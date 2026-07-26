from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from academics.models import Program
from .models import ProgramOutcome
from .services import calculate_po_attainment
from dashboard.models import Department
from .models import NBAMetric


def nba_dashboard(request):

    year = 2024
    programs = Program.objects.all()
    departments = Department.objects.all()

    dashboard_data = []
    department_data = []

    # --------------------------
    # PROGRAM LEVEL CALCULATION
    # --------------------------
    for program in programs:
        po_list = ProgramOutcome.objects.filter(program=program)

        po_data = []
        total_po_score = 0
        po_count = 0

        for po in po_list:
            attainment = calculate_po_attainment(po, year)

            if attainment >= 70:
                status = "Good"
            elif attainment >= 50:
                status = "Moderate"
            else:
                status = "Weak"

            total_po_score += attainment
            po_count += 1

            po_data.append({
                "code": po.code,
                "attainment": attainment,
                "status": status
            })

        if po_count > 0:
            program_score = round(total_po_score / po_count, 2)
        else:
            program_score = 0

        if program_score >= 80:
            program_status = "Excellent"
        elif program_score >= 65:
            program_status = "Good"
        elif program_score >= 50:
            program_status = "Moderate"
        else:
            program_status = "Critical"

        dashboard_data.append({
            "program": program.name,
            "department": program.department.name,
            "po_data": po_data,
            "program_score": program_score,
            "program_status": program_status
        })

    # --------------------------
    # DEPARTMENT LEVEL CALCULATION
    # --------------------------
    for dept in departments:
        dept_programs = programs.filter(department=dept)

        total_program_score = 0
        program_count = 0

        for program in dept_programs:
            po_list = ProgramOutcome.objects.filter(program=program)

            total_po_score = 0
            po_count = 0

            for po in po_list:
                attainment = calculate_po_attainment(po, year)
                total_po_score += attainment
                po_count += 1

            if po_count > 0:
                program_score = total_po_score / po_count
                total_program_score += program_score
                program_count += 1

        if program_count > 0:
            dept_score = round(total_program_score / program_count, 2)
        else:
            dept_score = 0

        if dept_score >= 80:
            dept_status = "Excellent"
        elif dept_score >= 65:
            dept_status = "Good"
        elif dept_score >= 50:
            dept_status = "Moderate"
        else:
            dept_status = "Critical"

        department_data.append({
            "department": dept.name,
            "dept_score": dept_score,
            "dept_status": dept_status
        })

    context = {
        "dashboard_data": dashboard_data,
        "department_data": department_data,
        "year": year
    }

    return render(request, "nba/dashboard.html", context)
from django.shortcuts import redirect
from .models import NBAMetric

def upload_nba_metric(request):
    if request.method == "POST":
        metric_id = request.POST.get("metric_id")
        file = request.FILES.get("file")

        metric = NBAMetric.objects.get(id=metric_id)
        metric.filled_file = file
        metric.save()

    return redirect("/intelligence/command-center/")
def download_nba_template(request, metric_id):
    metric = NBAMetric.objects.get(id=metric_id)

    template_path = metric.template_name

    html = render_to_string(template_path, {
    "metric": metric
    })

    response = HttpResponse(html, content_type='application/msword')
    response['Content-Disposition'] = f'attachment; filename="{metric.title}.doc"'

    return response