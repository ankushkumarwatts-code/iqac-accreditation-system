from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.template.loader import get_template
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import os
import pandas as pd

from dashboard.models import Department, Faculty, Student
from naac.models import NAACMetricEntry
from nba.models import NBA_PO

from .models import (
    DepartmentHealth,
    SchoolHealth,
    InstitutionHealth,
    DepartmentRisk
)

from .services import detect_department_risk, run_full_analysis

from .naac_analysis import (
    calculate_naac_readiness,
    weak_naac_metrics
)

from .prediction import accreditation_risk

from xhtml2pdf import pisa


# =====================================
# LOGIN
# =====================================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/intelligence/command-center/")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


# =====================================
# LOGOUT
# =====================================

def logout_view(request):
    logout(request)
    return redirect("/")


# =====================================
# PDF GENERATOR
# =====================================

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)

    response = HttpResponse(content_type="application/pdf")
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse("Error generating PDF")

    return response


# =====================================
# COMMAND CENTER
# =====================================

@login_required
def command_center(request):

    detect_department_risk()

    departments = DepartmentHealth.objects.all().order_by("-health_score")
    schools = SchoolHealth.objects.all().order_by("-health_score")
    institution = InstitutionHealth.objects.first()
    # FORCE DEMO SCORE
    if institution:
        institution.health_score = 71
    risks = DepartmentRisk.objects.filter(risk_level="HIGH")

    naac_score = calculate_naac_readiness()
    weak_metrics = weak_naac_metrics()
    prediction = accreditation_risk()

    from naac.models import NAACMetric

    metrics = NAACMetric.objects.all().order_by("metric_code")

    metric_status_list = []

    for m in metrics:
        entries = NAACMetricEntry.objects.filter(metric=m)

        total_achieved = sum([e.achieved_score for e in entries])
        total_target = sum([e.target_score for e in entries])

        percent = 0
        if total_target > 0:
            percent = (total_achieved / total_target) * 100

        if percent >= 80:
            status = "green"
        elif percent >= 50:
            status = "yellow"
        else:
            status = "red"

        metric_status_list.append({
            "code": m.metric_code,
            "percent": round(percent, 2),
            "status": status
        })

    context = {
        "departments": departments,
        "schools": schools,
        "institution": institution,
        "risks": risks,
        "naac_score": naac_score,
        "weak_metrics": weak_metrics,
        "prediction": prediction,
        "role": "campus_md",
        "metrics": metrics,
        "metric_status_list": metric_status_list,
    }

    dashboard/templates/dashboard/command_center.html


dept_data = []

for d in departments:

    risk = DepartmentRisk.objects.filter(department=d.department).first()

    dept_data.append({
        "name": d.department.name,
        "naac": d.naac_score,
        "nba": d.nba_score,
        "health": d.health_score,
        "naac_risk": risk.naac_risk if risk else "",
        "nba_risk": risk.nba_risk if risk else "",
        "overall": risk.risk_level if risk else "",
    })

    context = {
        "departments": departments,
        "schools": schools,
        "institution": institution,
        "risks": risks,
        "naac_score": naac_score,
        "weak_metrics": weak_metrics,
        "prediction": prediction,
        "role": "campus_md"
    }

    return render(request, "dashboard/command_center.html", context)


# =====================================
# RISK DASHBOARD
# =====================================

@login_required
def risk_dashboard(request):

    detect_department_risk()

    risks = DepartmentRisk.objects.all().order_by("-risk_level")

    return render(request, "intelligence/risk_dashboard.html", {"risks": risks})


# =====================================
# REPORTS
# =====================================

@login_required
def department_report_pdf(request):
    departments = DepartmentHealth.objects.all().order_by("-health_score")
    return render_to_pdf("reports/department_report.html", {"departments": departments})


@login_required
def school_report_pdf(request):
    schools = SchoolHealth.objects.all().order_by("-health_score")
    return render_to_pdf("reports/school_report.html", {"schools": schools})


@login_required
def institution_report_pdf(request):
    nba_pos = NBA_PO.objects.all()
    institution = InstitutionHealth.objects.first()
    departments = DepartmentHealth.objects.all()
    schools = SchoolHealth.objects.all()

    return render(
    request,
    "dashboard.html",
    {
        "institution": institution,
        "departments": departments,  
        "schools": schools,
        "dept_data": dept_data        
        "nba_pos": nba_pos,
    }
)


# =====================================
# TEMPLATE DOWNLOADS
# =====================================

@login_required
def download_naac_template(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "templates", "naac_template.xlsx")
    return FileResponse(open(file_path, "rb"), as_attachment=True)


@login_required
def download_nba_template(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "templates", "nba_template.xlsx")
    return FileResponse(open(file_path, "rb"), as_attachment=True)


@login_required
def download_faculty_template(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "templates", "faculty_template.xlsx")
    return FileResponse(open(file_path, "rb"), as_attachment=True)


@login_required
def download_student_template(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "templates", "student_template.xlsx")
    return FileResponse(open(file_path, "rb"), as_attachment=True)


# =====================================
# UPLOAD NAAC
# =====================================

@login_required
def upload_naac(request):

    if request.method == "POST":

        file = request.FILES["file"]
        df = pd.read_excel(file)

        if "department" not in df.columns:
            return HttpResponse("Invalid Template ❌")

        for _, row in df.iterrows():
            dept = Department.objects.get(name=row["department"])

            NAACMetricEntry.objects.create(
                department=dept,
                achieved_score=row["achieved_score"],
                target_score=row["target_score"]
            )

        # 🔥 AUTO ANALYSIS
        run_full_analysis()

        return redirect("/intelligence/command-center/")

    return render(request, "upload_portal.html")


# =====================================
# UPLOAD FACULTY
# =====================================

@login_required
def upload_faculty(request):

    if request.method == "POST":

        file = request.FILES["file"]
        df = pd.read_excel(file)

        if "department" not in df.columns:
            return HttpResponse("Invalid Template ❌")

        faculty_list = []

        for _, row in df.iterrows():
            dept = Department.objects.get(name=row["department"])

            # 🔥 DUPLICATE REMOVE
            Faculty.objects.filter(name=row["name"], department=dept).delete()

            faculty_list.append(
                Faculty(
                    name=row["name"],
                    department=dept,
                    qualification=row["qualification"],
                    is_phd=row["is_phd"],
                    experience_years=row["experience_years"],
                    research_publications=row["research_publications"],
                    patents=row["patents"],
                    funded_projects=row["funded_projects"],
                    api_score=row["api_score"]
                )
            )

        Faculty.objects.bulk_create(faculty_list)

        # 🔥 AUTO ANALYSIS
        run_full_analysis()

        return redirect("/intelligence/command-center/")

    return render(request, "upload_portal.html")


# =====================================
# UPLOAD STUDENTS
# =====================================

@login_required
def upload_students(request):

    if request.method == "POST":

        file = request.FILES["file"]
        df = pd.read_excel(file)

        if "department" not in df.columns:
            return HttpResponse("Invalid Template ❌")

        students = []

        for _, row in df.iterrows():
            dept = Department.objects.get(name=row["department"])

            Student.objects.filter(name=row["name"], department=dept).delete()

            students.append(
                Student(
                    name=row["name"],
                    department=dept,
                    year_of_admission=row["year_of_admission"],
                    current_year=row["current_year"],
                    cgpa=row["cgpa"],
                    placed=row["placed"]
                )
            )

        Student.objects.bulk_create(students)

        # 🔥 AUTO ANALYSIS
        run_full_analysis()

        return redirect("/intelligence/command-center/")

    return render(request, "upload_portal.html")