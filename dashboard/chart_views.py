# ============================================================
# chart_views.py
# dashboard/chart_views.py
# Part-1
# ============================================================

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from intelligence.charts import DashboardChartEngine


engine = DashboardChartEngine()


# ============================================================
# Institution Charts
# ============================================================

@login_required
def institution_health_chart(request):

    data = engine.institution_health_chart()

    return JsonResponse(data, safe=False)


@login_required
def institution_performance_chart(request):

    data = engine.institution_performance_trend_chart()

    return JsonResponse(data, safe=False)


@login_required
def institution_comparison_chart(request):

    data = engine.institution_comparison_chart()

    return JsonResponse(data, safe=False)


@login_required
def institution_school_chart(request):

    data = engine.institution_school_chart()

    return JsonResponse(data, safe=False)


# ============================================================
# School Charts
# ============================================================

@login_required
def school_health_chart(request):

    data = engine.school_health_chart()

    return JsonResponse(data, safe=False)


@login_required
def school_performance_chart(request):

    data = engine.school_performance_chart()

    return JsonResponse(data, safe=False)


@login_required
def school_comparison_chart(request):

    data = engine.school_comparison_chart()

    return JsonResponse(data, safe=False)


@login_required
def school_department_chart(request):

    data = engine.school_department_chart()

    return JsonResponse(data, safe=False)


# ============================================================
# Department Charts
# ============================================================

@login_required
def department_health_chart(request):

    data = engine.department_health_chart()

    return JsonResponse(data, safe=False)


@login_required
def department_performance_chart(request):

    data = engine.department_performance_trend_chart()

    return JsonResponse(data, safe=False)


@login_required
def department_comparison_chart(request):

    data = engine.department_comparison_chart()

    return JsonResponse(data, safe=False)


@login_required
def department_faculty_chart(request):

    data = engine.department_faculty_chart()

    return JsonResponse(data, safe=False)


# ============================================================
# Continue Part-2
# ============================================================
# ============================================================
# chart_views.py
# dashboard/chart_views.py
# Part-2
# ============================================================

# ============================================================
# Faculty Charts
# ============================================================

@login_required
def faculty_performance_chart(request):

    data = engine.faculty_performance_chart()

    return JsonResponse(data, safe=False)


@login_required
def faculty_performance_trend_chart(request):

    data = engine.faculty_performance_trend_chart()

    return JsonResponse(data, safe=False)


@login_required
def faculty_designation_chart(request):

    data = engine.faculty_designation_chart()

    return JsonResponse(data, safe=False)


@login_required
def faculty_department_distribution_chart(request):

    data = engine.faculty_department_distribution_chart()

    return JsonResponse(data, safe=False)


# ============================================================
# Student Charts
# ============================================================

@login_required
def student_distribution_chart(request):

    data = engine.student_distribution_chart()

    return JsonResponse(data, safe=False)


@login_required
def student_gender_distribution_chart(request):

    data = engine.student_gender_distribution_chart()

    return JsonResponse(data, safe=False)


@login_required
def student_year_distribution_chart(request):

    data = engine.student_year_distribution_chart()

    return JsonResponse(data, safe=False)


@login_required
def student_admission_trend_chart(request):

    data = engine.student_admission_trend_chart()

    return JsonResponse(data, safe=False)


# ============================================================
# KPI & Ranking Charts
# ============================================================

@login_required
def kpi_achievement_chart(request):

    data = engine.kpi_achievement_chart()

    return JsonResponse(data, safe=False)


@login_required
def ranking_chart(request):

    data = engine.ranking_chart()

    return JsonResponse(data, safe=False)


@login_required
def benchmark_chart(request):

    data = engine.benchmark_chart()

    return JsonResponse(data, safe=False)


@login_required
def average_health_chart(request):

    data = engine.average_health_chart()

    return JsonResponse(data, safe=False)


# ============================================================
# Continue Part-3
# ============================================================
# ============================================================
# chart_views.py
# dashboard/chart_views.py
# Part-3
# ============================================================

# ============================================================
# Risk Charts
# ============================================================

@login_required
def department_risk_chart(request):

    data = engine.department_risk_chart()

    return JsonResponse(data, safe=False)


@login_required
def risk_distribution_chart(request):

    data = engine.risk_distribution_chart()

    return JsonResponse(data, safe=False)


# ============================================================
# Score Charts
# ============================================================

@login_required
def overall_score_chart(request):

    data = engine.overall_score_chart()

    return JsonResponse(data, safe=False)


# ============================================================
# Analytics Charts
# ============================================================

@login_required
def analytics_summary_chart(request):

    data = engine.analytics_summary_chart()

    return JsonResponse(data, safe=False)


@login_required
def dashboard_summary_chart(request):

    data = engine.dashboard_summary_chart()

    return JsonResponse(data, safe=False)


@login_required
def overall_statistics_chart(request):

    data = engine.overall_statistics_chart()

    return JsonResponse(data, safe=False)


# ============================================================
# Executive Charts
# ============================================================

@login_required
def executive_dashboard_chart(request):

    data = engine.executive_dashboard_chart()

    return JsonResponse(data, safe=False)


@login_required
def executive_overview_chart(request):

    data = engine.executive_overview_chart()

    return JsonResponse(data, safe=False)


@login_required
def all_dashboard_charts(request):

    data = engine.all_dashboard_charts()

    return JsonResponse(data, safe=False)


# ============================================================
# Engine Information
# ============================================================

@login_required
def chart_engine_information(request):

    data = engine.engine_information()

    return JsonResponse(data, safe=False)


# ============================================================
# Health Check
# ============================================================

@login_required
def chart_health_check(request):

    return JsonResponse(
        {
            "status": "OK",
            "module": "Chart Engine",
            "version": "2.0"
        }
    )


# ============================================================
# Chart Count
# ============================================================

@login_required
def chart_count(request):

    charts = [
        "Institution Health",
        "Institution Performance",
        "Institution Comparison",
        "Institution School",
        "School Health",
        "School Performance",
        "School Comparison",
        "School Department",
        "Department Health",
        "Department Performance",
        "Department Comparison",
        "Department Faculty",
        "Faculty Performance",
        "Faculty Trend",
        "Faculty Designation",
        "Faculty Distribution",
        "Student Distribution",
        "Student Gender",
        "Student Year",
        "Student Admission Trend",
        "KPI Achievement",
        "Ranking",
        "Benchmark",
        "Average Health",
        "Department Risk",
        "Risk Distribution",
        "Overall Score",
        "Analytics Summary",
        "Dashboard Summary",
        "Overall Statistics",
        "Executive Dashboard",
        "Executive Overview"
    ]

    return JsonResponse(
        {
            "total_charts": len(charts),
            "charts": charts
        }
    )


# ============================================================
# END OF chart_views.py
# ============================================================