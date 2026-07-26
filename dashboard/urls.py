from django.urls import path

from . import views
from . import report_views
from . import chart_views

urlpatterns = [

    # ==========================================================
    # HOME
    # ==========================================================

    path(
        "",
        views.command_center,
        name="command_center",
    ),

    path(
        "dashboard/",
        views.executive_dashboard,
        name="executive_dashboard",
    ),

    path(
        "system-information/",
        views.system_information,
        name="system_information",
    ),

    # ==========================================================
    # INSTITUTION
    # ==========================================================

    path(
        "institution/<int:institution_id>/",
        views.institution_dashboard,
        name="institution_dashboard",
    ),

    path(
        "institution/list/",
        views.institution_list,
        name="institution_list",
    ),

    path(
        "institution/search/",
        views.search_institution,
        name="search_institution",
    ),

    # ==========================================================
    # SCHOOL
    # ==========================================================

    path(
        "school/<int:school_id>/",
        views.school_dashboard,
        name="school_dashboard",
    ),

    path(
        "school/list/",
        views.school_list,
        name="school_list",
    ),

    path(
        "school/search/",
        views.search_school,
        name="search_school",
    ),

    # ==========================================================
    # DEPARTMENT
    # ==========================================================

    path(
        "department/<int:department_id>/",
        views.department_dashboard,
        name="department_dashboard",
    ),

    path(
        "department/list/",
        views.department_list,
        name="department_list",
    ),

    path(
        "department/search/",
        views.search_department,
        name="search_department",
    ),

    # ==========================================================
    # FACULTY
    # ==========================================================

    path(
        "faculty/<int:faculty_id>/",
        views.faculty_dashboard,
        name="faculty_dashboard",
    ),

    path(
        "faculty/list/",
        views.faculty_list,
        name="faculty_list",
    ),

    path(
        "faculty/search/",
        views.search_faculty,
        name="search_faculty",
    ),

    # ==========================================================
    # STUDENT
    # ==========================================================

    path(
        "student/<int:student_id>/",
        views.student_dashboard,
        name="student_dashboard",
    ),

    path(
        "student/list/",
        views.student_list,
        name="student_list",
    ),

    path(
        "student/search/",
        views.search_student,
        name="search_student",
    ),

    # ==========================================================
    # ANALYTICS
    # ==========================================================

    path(
        "analytics/",
        views.analytics_dashboard,
        name="analytics_dashboard",
    ),

    # ==========================================================
    # KPI / BENCHMARK / RANKING
    # ==========================================================

    path(
        "kpi/",
        views.kpi_dashboard,
        name="kpi_dashboard",
    ),

    path(
        "benchmark/",
        views.benchmark_dashboard,
        name="benchmark_dashboard",
    ),

    path(
        "ranking/",
        views.ranking_dashboard,
        name="ranking_dashboard",
    ),

    path(
        "risk/",
        views.risk_dashboard,
        name="risk_dashboard",
    ),

    path(
        "ai/",
        views.ai_dashboard,
        name="ai_dashboard",
    ),

    # ==========================================================
    # REPORT HOME
    # ==========================================================

    path(
        "reports/",
        views.reports_home,
        name="reports_home",
    ),

    # ==========================================================
    # CONTINUED IN PART-2
    # ==========================================================
        # ==========================================================
    # INSTITUTION REPORTS
    # ==========================================================

    path(
        "reports/institution/pdf/",
        report_views.institution_pdf,
        name="institution_pdf",
    ),

    path(
        "reports/institution/excel/",
        report_views.institution_excel,
        name="institution_excel",
    ),

    path(
        "reports/institution/csv/",
        report_views.institution_csv,
        name="institution_csv",
    ),

    # ==========================================================
    # SCHOOL REPORTS
    # ==========================================================

    path(
        "reports/school/pdf/",
        report_views.school_pdf,
        name="school_pdf",
    ),

    path(
        "reports/school/excel/",
        report_views.school_excel,
        name="school_excel",
    ),

    path(
        "reports/school/csv/",
        report_views.school_csv,
        name="school_csv",
    ),

    # ==========================================================
    # DEPARTMENT REPORTS
    # ==========================================================

    path(
        "reports/department/pdf/",
        report_views.department_pdf,
        name="department_pdf",
    ),

    path(
        "reports/department/excel/",
        report_views.department_excel,
        name="department_excel",
    ),

    path(
        "reports/department/csv/",
        report_views.department_csv,
        name="department_csv",
    ),

    # ==========================================================
    # FACULTY REPORTS
    # ==========================================================

    path(
        "reports/faculty/pdf/",
        report_views.faculty_pdf,
        name="faculty_pdf",
    ),

    path(
        "reports/faculty/excel/",
        report_views.faculty_excel,
        name="faculty_excel",
    ),

    path(
        "reports/faculty/csv/",
        report_views.faculty_csv,
        name="faculty_csv",
    ),

    # ==========================================================
    # STUDENT REPORTS
    # ==========================================================

    path(
        "reports/student/pdf/",
        report_views.student_pdf,
        name="student_pdf",
    ),

    path(
        "reports/student/excel/",
        report_views.student_excel,
        name="student_excel",
    ),

    path(
        "reports/student/csv/",
        report_views.student_csv,
        name="student_csv",
    ),

    # ==========================================================
    # HEALTH REPORTS
    # ==========================================================

    path(
        "reports/institution-health/pdf/",
        report_views.institution_health_pdf,
        name="institution_health_pdf",
    ),

    path(
        "reports/institution-health/excel/",
        report_views.institution_health_excel,
        name="institution_health_excel",
    ),

    path(
        "reports/school-health/pdf/",
        report_views.school_health_pdf,
        name="school_health_pdf",
    ),

    path(
        "reports/school-health/excel/",
        report_views.school_health_excel,
        name="school_health_excel",
    ),

    path(
        "reports/department-health/pdf/",
        report_views.department_health_pdf,
        name="department_health_pdf",
    ),

    path(
        "reports/department-health/excel/",
        report_views.department_health_excel,
        name="department_health_excel",
    ),

    path(
        "reports/department-risk/pdf/",
        report_views.department_risk_pdf,
        name="department_risk_pdf",
    ),

    path(
        "reports/department-risk/excel/",
        report_views.department_risk_excel,
        name="department_risk_excel",
    ),

    # ==========================================================
    # EXECUTIVE REPORTS
    # ==========================================================

    path(
        "reports/executive/pdf/",
        report_views.executive_dashboard_pdf,
        name="executive_dashboard_pdf",
    ),

    path(
        "reports/executive/excel/",
        report_views.executive_dashboard_excel,
        name="executive_dashboard_excel",
    ),

    path(
        "reports/executive/csv/",
        report_views.executive_dashboard_csv,
        name="executive_dashboard_csv",
    ),

    # ==========================================================
    # DASHBOARD SUMMARY REPORTS
    # ==========================================================

    path(
        "reports/dashboard-summary/pdf/",
        report_views.dashboard_summary_pdf,
        name="dashboard_summary_pdf",
    ),

    path(
        "reports/dashboard-summary/excel/",
        report_views.dashboard_summary_excel,
        name="dashboard_summary_excel",
    ),

    path(
        "reports/dashboard-summary/csv/",
        report_views.dashboard_summary_csv,
        name="dashboard_summary_csv",
    ),

    # ==========================================================
    # REPORT INFORMATION
    # ==========================================================

    path(
        "reports/info/",
        report_views.report_information,
        name="report_information",
    ),

    path(
        "reports/health/",
        report_views.reports_health_check,
        name="reports_health_check",
    ),

    path(
        "reports/count/",
        report_views.report_count,
        name="report_count",
    ),

    # ==========================================================
    # CONTINUED IN PART-3 (ALL CHART URLS)
    # ==========================================================
        # ==========================================================
    # INSTITUTION CHARTS
    # ==========================================================

    path(
        "charts/institution/health/",
        chart_views.institution_health_chart,
        name="institution_health_chart",
    ),

    path(
        "charts/institution/performance/",
        chart_views.institution_performance_chart,
        name="institution_performance_chart",
    ),

    path(
        "charts/institution/comparison/",
        chart_views.institution_comparison_chart,
        name="institution_comparison_chart",
    ),

    path(
        "charts/institution/schools/",
        chart_views.institution_school_chart,
        name="institution_school_chart",
    ),

    # ==========================================================
    # SCHOOL CHARTS
    # ==========================================================

    path(
        "charts/school/health/",
        chart_views.school_health_chart,
        name="school_health_chart",
    ),

    path(
        "charts/school/performance/",
        chart_views.school_performance_chart,
        name="school_performance_chart",
    ),

    path(
        "charts/school/comparison/",
        chart_views.school_comparison_chart,
        name="school_comparison_chart",
    ),

    path(
        "charts/school/departments/",
        chart_views.school_department_chart,
        name="school_department_chart",
    ),

    # ==========================================================
    # DEPARTMENT CHARTS
    # ==========================================================

    path(
        "charts/department/health/",
        chart_views.department_health_chart,
        name="department_health_chart",
    ),

    path(
        "charts/department/performance/",
        chart_views.department_performance_chart,
        name="department_performance_chart",
    ),

    path(
        "charts/department/comparison/",
        chart_views.department_comparison_chart,
        name="department_comparison_chart",
    ),

    path(
        "charts/department/faculty/",
        chart_views.department_faculty_chart,
        name="department_faculty_chart",
    ),

    # ==========================================================
    # FACULTY CHARTS
    # ==========================================================

    path(
        "charts/faculty/performance/",
        chart_views.faculty_performance_chart,
        name="faculty_performance_chart",
    ),

    path(
        "charts/faculty/trend/",
        chart_views.faculty_performance_trend_chart,
        name="faculty_performance_trend_chart",
    ),

    path(
        "charts/faculty/designation/",
        chart_views.faculty_designation_chart,
        name="faculty_designation_chart",
    ),

    path(
        "charts/faculty/distribution/",
        chart_views.faculty_department_distribution_chart,
        name="faculty_department_distribution_chart",
    ),

    # ==========================================================
    # STUDENT CHARTS
    # ==========================================================

    path(
        "charts/student/distribution/",
        chart_views.student_distribution_chart,
        name="student_distribution_chart",
    ),

    path(
        "charts/student/gender/",
        chart_views.student_gender_distribution_chart,
        name="student_gender_distribution_chart",
    ),

    path(
        "charts/student/year/",
        chart_views.student_year_distribution_chart,
        name="student_year_distribution_chart",
    ),

    path(
        "charts/student/admission-trend/",
        chart_views.student_admission_trend_chart,
        name="student_admission_trend_chart",
    ),

    # ==========================================================
    # KPI / RANKING / BENCHMARK
    # ==========================================================

    path(
        "charts/kpi/",
        chart_views.kpi_achievement_chart,
        name="kpi_achievement_chart",
    ),

    path(
        "charts/ranking/",
        chart_views.ranking_chart,
        name="ranking_chart",
    ),

    path(
        "charts/benchmark/",
        chart_views.benchmark_chart,
        name="benchmark_chart",
    ),

    path(
        "charts/average-health/",
        chart_views.average_health_chart,
        name="average_health_chart",
    ),

    # ==========================================================
    # CONTINUED IN PART-4 (RISK, ANALYTICS, EXECUTIVE, METADATA)
    # ==========================================================
        # ==========================================================
    # RISK CHARTS
    # ==========================================================

    path(
        "charts/risk/department/",
        chart_views.department_risk_chart,
        name="department_risk_chart",
    ),

    path(
        "charts/risk/distribution/",
        chart_views.risk_distribution_chart,
        name="risk_distribution_chart",
    ),

    # ==========================================================
    # SCORE CHARTS
    # ==========================================================

    path(
        "charts/score/",
        chart_views.overall_score_chart,
        name="overall_score_chart",
    ),

    # ==========================================================
    # ANALYTICS CHARTS
    # ==========================================================

    path(
        "charts/analytics/summary/",
        chart_views.analytics_summary_chart,
        name="analytics_summary_chart",
    ),

    path(
        "charts/dashboard/summary/",
        chart_views.dashboard_summary_chart,
        name="dashboard_summary_chart",
    ),

    path(
        "charts/statistics/",
        chart_views.overall_statistics_chart,
        name="overall_statistics_chart",
    ),

    # ==========================================================
    # EXECUTIVE CHARTS
    # ==========================================================

    path(
        "charts/executive/",
        chart_views.executive_dashboard_chart,
        name="executive_dashboard_chart",
    ),

    path(
        "charts/executive/overview/",
        chart_views.executive_overview_chart,
        name="executive_overview_chart",
    ),

    path(
        "charts/all/",
        chart_views.all_dashboard_charts,
        name="all_dashboard_charts",
    ),

    # ==========================================================
    # CHART INFORMATION
    # ==========================================================

    path(
        "charts/info/",
        chart_views.chart_engine_information,
        name="chart_engine_information",
    ),

    path(
        "charts/health/",
        chart_views.chart_health_check,
        name="chart_health_check",
    ),

    path(
        "charts/count/",
        chart_views.chart_count,
        name="chart_count",
    ),

    # ==========================================================
    # END OF URLS
    # ==========================================================

]
