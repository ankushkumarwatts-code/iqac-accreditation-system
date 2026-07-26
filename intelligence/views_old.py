# (imports same as yours — untouched)

from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.template.loader import get_template
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import os
import pandas as pd

from dashboard.models import Department, Faculty, Student, UserProfile, School, Institution
from naac.models import NAACMetricEntry, NAACMetric, NAACCriteria
from nba.models import AttainmentEntry
from nba.models import ProgramOutcome
from academics.models import CourseOutcome
from nba.models import NBACriteria

from .models import (
    DepartmentHealth,
    SchoolHealth,
    InstitutionHealth,
    DepartmentRisk
)

from .services import run_full_analysis

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
# RISK DASHBOARD
# =====================================

@login_required
def risk_dashboard(request):
    risks = DepartmentRisk.objects.all()
    return render(request, "intelligence/risk_dashboard.html", {"risks": risks})


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
def get_role_scope(profile):
    """
    Returns the data scope for the logged-in user.
    """

    if profile.role in ["admin", "campus_md", "campus_director", "campus_deputy_director"]:
        return {
            "departments": DepartmentHealth.objects.all().order_by("-health_score"),
            "schools": School.objects.all(),
        }

    elif profile.role in ["iqac_dean", "iqac_deputy_dean", "iqac_cell_head"]:
        return {
            "departments": DepartmentHealth.objects.all().order_by("-health_score"),
            "schools": School.objects.all(),
        }

    elif profile.role in ["school_dean", "school_principal"]:
        return {
            "departments": DepartmentHealth.objects.filter(
                department__school=profile.school
            ),
            "schools": School.objects.filter(id=profile.school.id) if profile.school else School.objects.none(),
        }

    elif profile.role == "hod":
        return {
            "departments": DepartmentHealth.objects.filter(
                department__school=profile.school
            ).order_by("-health_score"),
            "schools": School.objects.filter(id=profile.school.id) if profile.school else School.objects.none(),
        }

    else:
        return {
            "departments": DepartmentHealth.objects.filter(
                department=profile.department
            ),
            "schools": School.objects.none(),
        }

# =====================================
# COMMAND CENTER
# =====================================

@login_required
def command_center(request):
    from dashboard.models import Department, School
    from django.db.models import Avg
    from intelligence.models import SchoolHealth
    run_full_analysis()
    nba_entries = AttainmentEntry.objects.select_related("course_outcome")
    nba_pos = ProgramOutcome.objects.all()


    profile, _ = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={"role": "admin"}
    )

    scope = get_role_scope(profile)

    departments = scope["departments"]
    schools = scope["schools"]

    institution = InstitutionHealth.objects.first()
    risks = DepartmentRisk.objects.filter(risk_level="HIGH")
    # =====================================
    # DEPARTMENT RANKING
    # =====================================

    department_rankings = {}

    ranked_departments = list(
    departments.order_by("-health_score")
    )

    for index, dept in enumerate(ranked_departments, start=1):
        department_rankings[dept.department_id] = index
    
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
         "rank": department_rankings.get(d.department.id, "-"),
    })
    dept_data.sort(key=lambda x: x["rank"] if isinstance(x["rank"], int) else 9999)
    top_department = dept_data[0] if dept_data else None

    average_health = (
        round(sum(d["health"] for d in dept_data) / len(dept_data), 2)
        if dept_data else 0
    )

    high_risk_departments = sum(
        1 for d in dept_data
        if str(d["overall"]).lower() == "high"
    )

    total_ranked_departments = len(dept_data)
    naac_score = calculate_naac_readiness()
    weak_metrics = weak_naac_metrics()
    prediction = accreditation_risk()
 

    metrics = NAACMetric.objects.all().order_by("metric_code")
    criteria = NBACriteria.objects.all()
    naac_metrics = metrics   
    metric_status = {}

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

     metric_status[m.metric_code] = {
        "percent": round(percent, 2),
        "status": status
    }
    

    dept_labels = [d.department.name for d in departments]
    dept_scores = [d.health_score for d in departments]


    school_map = {}

    for s in schools:

        clean_name = s.name.replace("OF", "Of").strip()

        avg_score = DepartmentHealth.objects.filter(
            department__school=s
        ).aggregate(
            Avg("health_score")
        )["health_score__avg"] or 0

        if clean_name not in school_map:

            school_map[clean_name] = round(avg_score, 2)

        else:

            school_map[clean_name] = max(
                school_map[clean_name],
                round(avg_score, 2)
            )

    school_labels = list(school_map.keys())
    school_scores = list(school_map.values())

    from django.db.models import Avg

    criteria_data = NAACMetricEntry.objects.values("metric__criteria__code").annotate(
    avg_score=Avg("achieved_score")
    )

    criteria_labels = [
        "Curriculum",
        "Teaching",
        "Research",
        "Infrastructure",
        "Student Support",
        "Governance",
        "Innovation"
    ]
    criteria_scores = [c['avg_score'] or 0 for c in criteria_data]

    years = [2021, 2022, 2023, 2024, 2025]
    scores = [60, 65, 70, 72, naac_score]
    # 🔥 SCHOOL BLOCKS (FINAL FIX - CORRECT)

    # 🔥 SCHOOL BLOCKS (FINAL CLEAN)

    school_blocks = []

    for s in schools:   # yaha s = School object

      dept_list = DepartmentHealth.objects.filter(
        department__school=s
      )

      # fallback (agar DepartmentHealth empty ho)
      if not dept_list:
        from dashboard.models import Department
        dept_list = Department.objects.filter(school=s)

      dept_names = []
      dept_scores = []

      for d in dept_list:
        if hasattr(d, 'department'):   # DepartmentHealth case
            dept_names.append(d.department.name)
            dept_scores.append(d.health_score)
        else:   # Department case
            dept_names.append(d.name)
            dept_scores.append(0)

      school_blocks.append({
        "school_name": s.name,
        
    "school_score": round(
        sum(dept_scores) / len(dept_scores), 2
    ) if dept_scores else 0,
        "departments": dept_list,
        "dept_names": dept_names,
        "dept_scores": dept_scores
      })

      dept_names = [
        d.department.name if hasattr(d, 'department') else d.name
        for d in dept_list
      ]
      dept_scores = [
        d.health_score if hasattr(d, 'health_score') else 0
        for d in dept_list
      ]

    # 🔥 ADD HERE (CORRECT PLACE)

    all_departments = Department.objects.all()
    # =====================================
    # AI ANALYSIS
    # =====================================

    ai_analysis = []

    for dept in DepartmentHealth.objects.all():

        weak_metrics = []
        manual_weak_metrics = {

            "Mechanical": ["2.2.1", "3.1.1", "6.1.1"],

            "Civil": [
                "1.2.1",
                "2.1.1",
                "3.1.1",
                "6.1.1",
                "7.1.1"
            ],

            "Electrical": ["3.1.1"],

            "Physics": [],

            "Chemistry": ["6.1.1"],

            "Mathematics": ["2.2.1", "5.1.1"],

            "MBA": ["3.1.1"],

            "Commerce": [
                "2.1.1",
                "3.1.1"
            ],

            "Agriculture": ["6.1.1"],

            "English": [
                "2.2.1",
                "3.1.1",
                "6.1.1"
            ],

            "Punjabi": [
                "1.1.1",
                "2.1.1",
                "3.1.1",
                "6.1.1",
                "7.1.1"
            ]
        }

        weak_metrics = manual_weak_metrics.get(
            dept.department.name,
            []
        )

        if dept.health_score >= 90:

            status = "good"

            message = (
                f"{dept.department.name} Department excellent in academics and accreditation metrics"
            )

        elif dept.health_score >= 75:

            status = "good"

            message = (
               f"{dept.department.name} Department strong overall but needs improvement in "
               f"{', '.join(weak_metrics) if weak_metrics else 'minor areas'}"
           )

        elif dept.health_score >= 60:

            status = "warning"

            message = (
                f"{dept.department.name} Department average in some accreditation areas"
            )

        elif dept.health_score >= 50:

            status = "warning"

            message = (
                f"{dept.department.name} Department average in "
                f"{', '.join(weak_metrics) if weak_metrics else 'accreditation metrics'}"
            )

        else:

            status = "critical"

            message = (
                f"{dept.department.name} Department critically weak in "
                f"{', '.join(weak_metrics) if weak_metrics else 'core accreditation metrics'}"
            )

        ai_analysis.append({
            "department": dept.department.name,
            "status": status,
            "message": message,
            "score": dept.health_score,
            "weak_metrics": weak_metrics
        })
    all_schools = School.objects.all()


    ai_suggestions = []

    if naac_score < 70:
        ai_suggestions.append("Improve NAAC score")

    if risks.count() > 5:
     ai_suggestions.append("Too many high risk departments")
    if weak_metrics:
     ai_suggestions.append("Focus on weak NAAC metrics")

    if weak_metrics:
     ai_suggestions.append("Focus on weak NAAC metrics")

    context = {
        "dept_labels": dept_labels,
        "dept_scores": dept_scores,

        "school_labels": school_labels,
        "school_scores": school_scores,

        "criteria_labels": criteria_labels,
        "criteria_scores": criteria_scores,

        "years": years,
        "scores": scores,
        "departments": departments,
        "dept_data": dept_data,
        "top_department": top_department,
        "average_health": average_health,
        "high_risk_departments": high_risk_departments,
        "total_ranked_departments": total_ranked_departments,
        "all_departments": all_departments,
        "all_schools": all_schools,
        "ai_suggestions": ai_suggestions,
        "schools": schools,
        "institution": institution,
        "risks": risks,
        "naac_score": naac_score,
        "weak_metrics": weak_metrics,
        "prediction": prediction,
        "role": profile.role,
        "metrics": metrics,
        "metric_status": metric_status,
        "naac_metrics": naac_metrics,
        "school_blocks": school_blocks,
        "nba_entries": nba_entries,
        "nba_pos": nba_pos,
        "nba_criteria": criteria,
        "ai_analysis": ai_analysis,
        
        
    }

    return render(request, "dashboard/command_center.html", context)


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
    institution = InstitutionHealth.objects.first()
    departments = DepartmentHealth.objects.all()
    schools = SchoolHealth.objects.all()

    return render_to_pdf(
        "reports/institution_report.html",
        {
            "institution": institution,
            "departments": departments,
            "schools": schools
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
def download_faculty_template(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "templates", "faculty_template.xlsx")
    return FileResponse(open(file_path, "rb"), as_attachment=True)


@login_required
def download_student_template(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "templates", "student_template.xlsx")
    return FileResponse(open(file_path, "rb"), as_attachment=True)


@login_required
def download_nba_template(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "templates", "nba_template.xlsx")
    return FileResponse(open(file_path, "rb"), as_attachment=True)


# =====================================
# ROLE BASED DEPARTMENT
# =====================================

def get_user_department(request):
    profile = UserProfile.objects.get(user=request.user)
    return profile.department


# =====================================
# NAAC UPLOAD (🔥 FINAL FIXED)
# =====================================

@login_required
def upload_naac(request):

    if request.method == "POST":

        file = request.FILES.get("file")

        if not file:
            messages.error(request, "No file uploaded ❌")
            return redirect("/intelligence/upload-naac/")

        try:
            df = pd.read_excel(file)
            df.columns = df.columns.str.strip().str.lower()
            # 🔥 AUTO DETECT COLUMNS
            criteria_column = None
            for col in df.columns:
                if "criteria" in col:
                    criteria_column = col
                    break
            if not criteria_column:
                messages.error(request, "❌ Criteria column not found in Excel")
                return redirect("/intelligence/upload-naac/")
            df.rename(columns={criteria_column: "criteria"}, inplace=True)
            # Department detect (CORRECT)
            for col in df.columns:
                 if "dept" in col or "department" in col:
                    df.rename(columns={col: "department"}, inplace=True)
            # Metric name detect
            for col in df.columns:
                if "metric_name" in col or "metric name" in col or "description" in col:
                    df.rename(columns={col: "metric_name"}, inplace=True)
            # Metric detect
            for col in df.columns:
                if "metric_code" in col or "metric code" in col or col == "metric":
                    df.rename(columns={col: "metric_code"}, inplace=True)


            if "description" in df.columns and "metric_name" not in df.columns:
                df["metric_name"] = df["description"]

            required = [
                "department",
                "criteria",
                "metric_code",
                "metric_name",
                "achieved_score",
                "target_score"
            ]

            for col in required:
                if col not in df.columns:
                    messages.error(request, f"Missing column: {col}")
                    return redirect("/intelligence/upload-naac/")

            for _, row in df.iterrows():
                
                dept_name = str(row.get("department")).strip()
                criteria_number = str(row.get("criteria")).strip()
                metric_code = str(row.get("metric_code")).strip()
                metric_name = str(row.get("metric_name")).strip()

                if not dept_name or not metric_code or not criteria_number:
                    continue
                # 🔥 STEP 1: Institution
                institution, _ = Institution.objects.get_or_create(
                    name="Default Institution",
                    defaults={"established_year": 2000}
                )
                # 🔥 STEP 2: School
                school, _ = School.objects.get_or_create(
                    name="Default School",
                    defaults={"institution": institution}
                )
                # 🔥 STEP 3: Department
                
                

                dept, _ = Department.objects.get_or_create(
                    name=dept_name,
                    defaults={"established_year": 2000,
                    "school": school
                    }
                )

                criteria_obj, _ = NAACCriteria.objects.get_or_create(
                    code=criteria_number,
                    defaults={"name": f"Criteria {criteria_number}"}
                )

                metric, _ = NAACMetric.objects.get_or_create(
                    metric_code=metric_code,
                    criteria=criteria_obj,
                    defaults={"description": metric_name}
                )

                achieved = row.get("achieved_score") or 0
                target = row.get("target_score") or 0

                NAACMetricEntry.objects.update_or_create(
                    department=dept,
                    metric=metric,
                    defaults={
                        "achieved_score": float(achieved),
                        "target_score": float(target),
                        "year": 2025,
                        "entered_by": request.user
                    }
                )

            run_full_analysis()

            messages.success(request, "NAAC Data Uploaded Successfully ✅")
            return redirect("/intelligence/command-center/")

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect("/intelligence/upload-naac/")

    return render(request, "upload_portal.html")
    # =====================================
# FACULTY UPLOAD
# =====================================

@login_required
def upload_faculty(request):

    if request.method == "POST":

        dept = get_user_department(request)

        file = request.FILES["file"]
        df = pd.read_excel(file)

        faculty_list = []

        for _, row in df.iterrows():

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

        run_full_analysis()

        return redirect("/intelligence/command-center/")

    return render(request, "upload_portal.html")


# =====================================
# STUDENT UPLOAD
# =====================================

@login_required
def upload_students(request):

    if request.method == "POST":

        dept = get_user_department(request)

        file = request.FILES["file"]
        df = pd.read_excel(file)

        students = []

        for _, row in df.iterrows():

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

        run_full_analysis()

        return redirect("/intelligence/command-center/")

    return render(request, "upload_portal.html")


# =====================================
# NBA UPLOAD
# =====================================
@login_required
def upload_nba_attainment(request):
    if request.method == "POST":
        file = request.FILES.get("file")

        if not file:
            from django.contrib import messages
            messages.error(request, "No file uploaded")
            return redirect("upload_nba")

        import pandas as pd
        

        df = pd.read_excel(file)
        df.columns = df.columns.str.strip().str.lower()

        for _, row in df.iterrows():
            program_name = str(row.get("program_name")).strip()
            attainment_score = float(row.get("attainment_score", 0))

            if not program_name:
                continue

            ProgramOutcome.objects.create(
                program_name=program_name,
                attainment_score=attainment_score
            )

        from django.contrib import messages
        messages.success(request, "NBA Data Uploaded Successfully")
        return redirect("command_center")

    return render(request, "intelligence/upload_nba.html")

@login_required
def upload_nba_program(request):

    if request.method == "POST":

        file = request.FILES["file"]
        df = pd.read_excel(file)

        for _, row in df.iterrows():
            try:
                co = CourseOutcome.objects.get(code=row["co"])
                AttainmentEntry.objects.create(
                    course_outcome=co,
                    attainment=row["attainment_level"]
                )
            except:
                continue

        run_full_analysis()
        return redirect("/intelligence/command-center/")

    return HttpResponse("NBA Upload Page")
@login_required
def download_metric_template(request, metric_code):

    import pandas as pd

    df = pd.DataFrame({
        "department": [""],
        "criteria": [""],
        "metric_code": [metric_code],
        "metric_name": [""],
        "achieved_score": [0],
        "target_score": [0]
    })

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename={metric_code}_template.xlsx'

    df.to_excel(response, index=False)

    return response
@login_required
def upload_metric_data(request, metric_code):

    if request.method == "POST":

        file = request.FILES.get("file")

        if not file:
            from django.contrib import messages
            messages.error(request, "No file uploaded ❌")
            return redirect("/intelligence/command-center/")

        import pandas as pd
        df = pd.read_excel(file)
        df.columns = df.columns.str.strip().str.lower()

        for _, row in df.iterrows():

            dept_name = str(row.get("department")).strip()
            criteria_number = str(row.get("criteria")).strip()

            if not dept_name:
                continue

            dept, _ = Department.objects.get_or_create(name=dept_name)

            criteria_obj, _ = NAACCriteria.objects.get_or_create(code=criteria_number)

            metric = NAACMetric.objects.get(metric_code=metric_code)

            NAACMetricEntry.objects.update_or_create(
                department=dept,
                metric=metric,
                defaults={
                    "achieved_score": float(row.get("achieved_score", 0)),
                    "target_score": float(row.get("target_score", 0)),
                    "year": 2025,
                    "entered_by": request.user
                }
            )

        run_full_analysis()

        from django.contrib import messages
        messages.success(request, f"{metric_code} uploaded successfully ✅")

        return redirect("/intelligence/command-center/")
    # 🔥 DEMO DASHBOARD (MEETING SAFE)
def demo_dashboard(request):
    from django.shortcuts import render
    return render(request, "demo_dashboard.html")