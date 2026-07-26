from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import NAACCriteria, NAACMetric
from .services import calculate_criteria_percentage, calculate_overall_naac_score

def naac_dashboard(request):

    selected_year = request.GET.get("year")
    if selected_year:
        year = int(selected_year)
    else:
        year = 2024

    previous_year = year - 1

    criteria_list = NAACCriteria.objects.all()
    criteria_data = []
    critical_count = 0

    for criteria in criteria_list:
        percentage = calculate_criteria_percentage(criteria, year)

        if percentage >= 85:
            status = "Green"
        elif percentage >= 70:
            status = "Yellow"
        else:
            status = "Red"

        if percentage < 60:
            critical_count += 1

        criteria_data.append({
            "code": criteria.code,
            "name": criteria.name,
            "percentage": percentage,
            "status": status
        })

    # Weakest detection
    weakest_criteria = None
    lowest_score = 101

    for c in criteria_data:
        if c["percentage"] < lowest_score:
            lowest_score = c["percentage"]
            weakest_criteria = c["code"]

    overall_score = calculate_overall_naac_score(year)

    # Growth logic
    previous_score = calculate_overall_naac_score(previous_year)

    if previous_score and previous_score > 0:
        growth = round(overall_score - previous_score, 2)

        if growth > 0:
            growth_status = "up"
        elif growth < 0:
            growth_status = "down"
        else:
            growth_status = "same"
    else:
        growth = None
        growth_status = "no_data"

    # Grade prediction
    if overall_score >= 85:
        predicted_grade = "A++"
    elif overall_score >= 75:
        predicted_grade = "A+"
    elif overall_score >= 65:
        predicted_grade = "A"
    elif overall_score >= 55:
        predicted_grade = "B++"
    elif overall_score >= 45:
        predicted_grade = "B+"
    else:
        predicted_grade = "C"

    # 🔥 Institutional Health Index
    health_index = round(overall_score - (critical_count * 5), 2)

    if health_index >= 80:
        health_status = "Excellent"
    elif health_index >= 60:
        health_status = "Stable"
    elif health_index >= 40:
        health_status = "Warning"
    else:
        health_status = "Critical"

    context = {
        "overall_score": overall_score,
        "predicted_grade": predicted_grade,
        "criteria_data": criteria_data,
        "critical_count": critical_count,
        "total_criteria": criteria_list.count(),
        "weakest_criteria": weakest_criteria,
        "selected_year": year,
        "growth": growth,
        "growth_status": growth_status,
        "health_index": health_index,
        "health_status": health_status
    }

    return render(request, "naac/dashboard.html", context)
def download_naac_template(request, metric_id):
    metric = NAACMetric.objects.get(id=metric_id)

    template_path = metric.template_name

    html = render_to_string(template_path, {
        "metric": metric
    })

    response = HttpResponse(html, content_type='application/msword')
    response['Content-Disposition'] = f'attachment; filename="{metric.metric_code}.doc"'

    return response
def download_naac_template(request, metric_id):
    metric = NAACMetric.objects.get(id=metric_id)

    template_path = metric.template_name

    html = render_to_string(template_path, {
        "metric": metric
    })

    response = HttpResponse(html, content_type='application/msword')
    response['Content-Disposition'] = f'attachment; filename="{metric.metric_code}.doc"'

    return response
def download_naac_template(request, metric_id):
    metric = NAACMetric.objects.get(id=metric_id)

    template_path = metric.template_name

    html = render_to_string(template_path, {
        "metric": metric
    })

    response = HttpResponse(html, content_type='text/html')
    response['Content-Disposition'] = f'attachment; filename="{metric.metric_code}.html"'

    return response