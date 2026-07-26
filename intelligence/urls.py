# ============================================================
# urls.py
# Institutional Brain Dashboard
# PART - 1 / 6
# ============================================================

from django.urls import path
from . import views_upload
from . import views_dashboard
from . import api_views
from . import views_reports
from django.urls import path
from . import views


urlpatterns = [

# ============================================================
# Dashboard Home
# ============================================================

path(
    "",
    views_dashboard.dashboard_home,
    name="dashboard_home",
),

path(
    "command-center/",
    views_dashboard.command_center,
    name="command_center",
),

path(
    "system-information/",
    views_dashboard.system_information,
    name="system_information",
),

# ============================================================
# Institution Dashboard
# ============================================================

path(
    "institution/<int:institution_id>/",
    views_dashboard.institution_dashboard,
    name="institution_dashboard",
),

# ============================================================
# School Dashboard
# ============================================================

path(
    "school/<int:school_id>/",
    views_dashboard.school_dashboard,
    name="school_dashboard",
),

# ============================================================
# Department Dashboard
# ============================================================

path(
    "department/<int:department_id>/",
    views_dashboard.department_dashboard,
    name="department_dashboard",
),

# ============================================================
# Lists
# ============================================================

path(
    "institutions/",
    views_dashboard.institution_list,
    name="institution_list",
),

path(
    "schools/",
    views_dashboard.school_list,
    name="school_list",
),

path(
    "departments/",
    views_dashboard.department_list,
    name="department_list",
),

path(
    "faculty/",
    views_dashboard.faculty_list,
    name="faculty_list",
),

path(
    "students/",
    views_dashboard.student_list,
    name="student_list",
),

# ============================================================
# Search Views
# ============================================================

path(
    "search/institution/",
    views_dashboard.search_institution,
    name="search_institution",
),

path(
    "search/school/",
    views_dashboard.search_school,
    name="search_school",
),

path(
    "search/department/",
    views_dashboard.search_department,
    name="search_department",
),

path(
    "search/faculty/",
    views_dashboard.search_faculty,
    name="search_faculty",
),

path(
    "search/student/",
    views_dashboard.search_student,
    name="search_student",
),

# ============================================================
# Dashboard APIs
# ============================================================

path(
    "api/dashboard/",
    api_views.dashboard_api,
    name="dashboard_api",
),

path(
    "api/executive-dashboard/",
    api_views.executive_dashboard_api,
    name="executive_dashboard_api",
),

path(
    "api/system-report/",
    api_views.system_report_api,
    name="system_report_api",
),

path(
    "api/dashboard-statistics/",
    api_views.dashboard_statistics_api,
    name="dashboard_statistics_api",
),

path(
    "api/system-snapshot/",
    api_views.system_snapshot_api,
    name="system_snapshot_api",
),

path(
    "api/system-Strength/",
    api_views.system_health_report_api,
    name="system_health_report_api",
),

path(
    "api/dashboard-status/",
    api_views.dashboard_status_api,
    name="dashboard_status_api",
),

path(
    "api/dashboard-version/",
    api_views.dashboard_version_api,
    name="dashboard_version_api",
),

path(
    "api/dashboard-configuration/",
    api_views.dashboard_configuration_api,
    name="dashboard_configuration_api",
),

path(
    "api/dashboard-information/",
    api_views.dashboard_information_api,
    name="dashboard_information_api",
),

path(
    "api/dashboard-modules/",
    api_views.dashboard_modules_api,
    name="dashboard_modules_api",
),

path(
    "api/dashboard-engines/",
    api_views.dashboard_engines_api,
    name="dashboard_engines_api",
),

path(
    "api/dashboard-services/",
    api_views.dashboard_services_api,
    name="dashboard_services_api",
),

path(
    "api/engine-information/",
    api_views.engine_information_api,
    name="engine_information_api",
),

# ===================== END PART-1 =====================
# ============================================================
# urls.py
# Institutional Brain Dashboard
# PART - 2 / 6
# ============================================================

# ============================================================
# Institution APIs
# ============================================================

path(
    "api/institution/<int:institution_id>/",
    api_views.institution_api,
    name="institution_api",
),

path(
    "api/institutions/",
    api_views.institution_list_api,
    name="institution_list_api",
),

path(
    "api/institution-count/",
    api_views.institution_count_api,
    name="institution_count_api",
),

path(
    "api/institution-Strength/<int:institution_id>/",
    api_views.institution_health_api,
    name="institution_health_api",
),

# ============================================================
# School APIs
# ============================================================

path(
    "api/school/<int:school_id>/",
    api_views.school_api,
    name="school_api",
),

path(
    "api/schools/",
    api_views.school_list_api,
    name="school_list_api",
),

path(
    "api/school-count/",
    api_views.school_count_api,
    name="school_count_api",
),

path(
    "api/school-Strength/<int:school_id>/",
    api_views.school_health_api,
    name="school_health_api",
),

# ============================================================
# Department APIs
# ============================================================

path(
    "api/department/<int:department_id>/",
    api_views.department_api,
    name="department_api",
),

path(
    "api/departments/",
    api_views.department_list_api,
    name="department_list_api",
),

path(
    "api/department-count/",
    api_views.department_count_api,
    name="department_count_api",
),

path(
    "api/department-Strength/<int:department_id>/",
    api_views.department_health_api,
    name="department_health_api",
),

path(
    "api/department-risk/<int:department_id>/",
    api_views.department_risk_api,
    name="department_risk_api",
),

# ============================================================
# Faculty APIs
# ============================================================

path(
    "api/faculty/<int:faculty_id>/",
    api_views.faculty_api,
    name="faculty_api",
),

path(
    "api/faculties/",
    api_views.faculty_list_api,
    name="faculty_list_api",
),

path(
    "api/faculty-count/",
    api_views.faculty_count_api,
    name="faculty_count_api",
),

path(
    "api/faculty-summary/",
    api_views.faculty_summary_api,
    name="faculty_summary_api",
),

# ============================================================
# Student APIs
# ============================================================

path(
    "api/student/<int:student_id>/",
    api_views.student_api,
    name="student_api",
),

path(
    "api/students/",
    api_views.student_list_api,
    name="student_list_api",
),

path(
    "api/student-count/",
    api_views.student_count_api,
    name="student_count_api",
),

path(
    "api/student-summary/",
    api_views.student_summary_api,
    name="student_summary_api",
),

# ===================== END PART-2 =====================
# ============================================================
# urls.py
# Institutional Brain Dashboard
# PART - 3 / 6
# ============================================================

# ============================================================
# Strength & Risk Summary APIs
# ============================================================

path(
    "api/Strength-summary/",
    api_views.health_summary_api,
    name="health_summary_api",
),

path(
    "api/risk-summary/",
    api_views.risk_summary_api,
    name="risk_summary_api",
),

path(
    "api/performance-summary/",
    api_views.performance_summary_api,
    name="performance_summary_api",
),

path(
    "api/governance-summary/",
    api_views.governance_summary_api,
    name="governance_summary_api",
),

path(
    "api/user-summary/",
    api_views.user_summary_api,
    name="user_summary_api",
),

path(
    "api/quick-statistics/",
    api_views.quick_statistics_api,
    name="quick_statistics_api",
),

# ============================================================
# Executive APIs
# ============================================================

path(
    "api/executive-report/",
    api_views.executive_report_api,
    name="executive_report_api",
),

path(
    "api/executive-dashboard-summary/",
    api_views.executive_dashboard_summary_api,
    name="executive_dashboard_summary_api",
),

path(
    "api/export-dashboard/",
    api_views.export_dashboard_api,
    name="export_dashboard_api",
),

path(
    "api/institution-directory/",
    api_views.institution_directory_api,
    name="institution_directory_api",
),

# ============================================================
# Search APIs
# ============================================================

path(
    "api/search/institution/",
    api_views.search_institution_api,
    name="search_institution_api",
),

path(
    "api/search/school/",
    api_views.search_school_api,
    name="search_school_api",
),

path(
    "api/search/department/",
    api_views.search_department_api,
    name="search_department_api",
),

path(
    "api/search/faculty/",
    api_views.search_faculty_api,
    name="search_faculty_api",
),

path(
    "api/search/student/",
    api_views.search_student_api,
    name="search_student_api",
),

# ============================================================
# Utility APIs
# ============================================================

path(
    "api/current-user/",
    api_views.current_user_api,
    name="current_user_api",
),

path(
    "api/ping/",
    api_views.ping_api,
    name="ping_api",
),

path(
    "api/dashboard-metadata/",
    api_views.dashboard_metadata_api,
    name="dashboard_metadata_api",
),

# ===================== END PART-3 =====================
# ============================================================
# urls.py
# Institutional Brain Dashboard
# PART - 4 / 6
# ============================================================

# ============================================================
# Dashboard Feature APIs
# (Implemented in views_dashboard.py)
# ============================================================

path(
    "api/dashboard-summary/",
    views_dashboard.dashboard_summary_api,
    name="dashboard_summary_api",
),

path(
    "api/dashboard-chart/",
    views_dashboard.dashboard_chart_api,
    name="dashboard_chart_api",
),

path(
    "api/dashboard-ranking/",
    views_dashboard.dashboard_ranking_api,
    name="dashboard_ranking_api",
),

path(
    "api/dashboard-kpi/",
    views_dashboard.dashboard_kpi_api,
    name="dashboard_kpi_api",
),

path(
    "api/dashboard-benchmark/",
    views_dashboard.dashboard_benchmark_api,
    name="dashboard_benchmark_api",
),

path(
    "api/dashboard-risk/",
    views_dashboard.dashboard_risk_api,
    name="dashboard_risk_api",
),

path(
    "api/dashboard-ai/",
    views_dashboard.dashboard_ai_api,
    name="dashboard_ai_api",
),

path(
    "api/dashboard-analytics/",
    views_dashboard.dashboard_analytics_api,
    name="dashboard_analytics_api",
),

path(
    "api/dashboard-mapping/",
    views_dashboard.dashboard_mapping_api,
    name="dashboard_mapping_api",
),

path(
    "api/dashboard-score/",
    views_dashboard.dashboard_score_api,
    name="dashboard_score_api",
),

# ============================================================
# Dashboard Overview APIs
# ============================================================

path(
    "api/Strength-overview/",
    views_dashboard.health_overview_api,
    name="health_overview_api",
),

path(
    "api/risk-overview/",
    views_dashboard.risk_overview_api,
    name="risk_overview_api",
),

# ============================================================
# Dashboard Detail APIs
# ============================================================

path(
    "api/institution-dashboard/<int:institution_id>/",
    views_dashboard.institution_api,
    name="institution_dashboard_api",
),

path(
    "api/school-dashboard/<int:school_id>/",
    views_dashboard.school_api,
    name="school_dashboard_api",
),

path(
    "api/department-dashboard/<int:department_id>/",
    views_dashboard.department_api,
    name="department_dashboard_api",
),

# ===================== END PART-4 =====================
# ============================================================
# urls.py
# Institutional Brain Dashboard
# PART - 5 / 6
# ============================================================

# ============================================================
# Dashboard Information APIs
# ============================================================

path(
    "api/dashboard-information/",
    api_views.dashboard_information_api,
    name="dashboard_information_api",
),

path(
    "api/dashboard-version/",
    api_views.dashboard_version_api,
    name="dashboard_version_api",
),

path(
    "api/dashboard-configuration/",
    api_views.dashboard_configuration_api,
    name="dashboard_configuration_api",
),

path(
    "api/dashboard-modules/",
    api_views.dashboard_modules_api,
    name="dashboard_modules_api",
),

path(
    "api/dashboard-engines/",
    api_views.dashboard_engines_api,
    name="dashboard_engines_api",
),

path(
    "api/dashboard-services/",
    api_views.dashboard_services_api,
    name="dashboard_services_api",
),

path(
    "api/engine-information/",
    api_views.engine_information_api,
    name="engine_information_api",
),

# ============================================================
# Dashboard Count APIs
# ============================================================

path(
    "api/institution-count/",
    api_views.institution_count_api,
    name="institution_count_api",
),

path(
    "api/school-count/",
    api_views.school_count_api,
    name="school_count_api",
),

path(
    "api/department-count/",
    api_views.department_count_api,
    name="department_count_api",
),

path(
    "api/faculty-count/",
    api_views.faculty_count_api,
    name="faculty_count_api",
),

path(
    "api/student-count/",
    api_views.student_count_api,
    name="student_count_api",
),

# ============================================================
# Dashboard Status APIs
# ============================================================

path(
    "api/dashboard-status/",
    api_views.dashboard_status_api,
    name="dashboard_status_api",
),

path(
    "api/ping/",
    api_views.ping_api,
    name="ping_api",
),

path(
    "api/current-user/",
    api_views.current_user_api,
    name="current_user_api",
),

path(
    "api/dashboard-metadata/",
    api_views.dashboard_metadata_api,
    name="dashboard_metadata_api",
),

# ===================== END PART-5 =====================
# ============================================================
# urls.py
# Institutional Brain Dashboard
# PART - 6 / 6
# ============================================================

# ============================================================
# Miscellaneous APIs
# ============================================================

path(
    "api/dashboard-summary/",
    views_dashboard.dashboard_summary_api,
    name="dashboard_summary_api",
),

path(
    "api/Strength-overview/",
    views_dashboard.health_overview_api,
    name="health_overview_api",
),

path(
    "api/risk-overview/",
    views_dashboard.risk_overview_api,
    name="risk_overview_api",
),

# ============================================================
# Dashboard Detail APIs
# ============================================================

path(
    "api/institution-dashboard/<int:institution_id>/",
    views_dashboard.institution_api,
    name="institution_dashboard_api",
),

path(
    "api/school-dashboard/<int:school_id>/",
    views_dashboard.school_api,
    name="school_dashboard_api",
),

path(
    "api/department-dashboard/<int:department_id>/",
    views_dashboard.department_api,
    name="department_dashboard_api",
),

# ============================================================
# Dashboard Feature APIs
# (Implemented in views_dashboard.py)
# ============================================================

path(
    "api/dashboard-chart/",
    views_dashboard.dashboard_chart_api,
    name="dashboard_chart_api",
),

path(
    "api/dashboard-ranking/",
    views_dashboard.dashboard_ranking_api,
    name="dashboard_ranking_api",
),

path(
    "api/dashboard-kpi/",
    views_dashboard.dashboard_kpi_api,
    name="dashboard_kpi_api",
),

path(
    "api/dashboard-benchmark/",
    views_dashboard.dashboard_benchmark_api,
    name="dashboard_benchmark_api",
),

path(
    "api/dashboard-risk/",
    views_dashboard.dashboard_risk_api,
    name="dashboard_risk_api",
),

path(
    "api/dashboard-ai/",
    views_dashboard.dashboard_ai_api,
    name="dashboard_ai_api",
),

path(
    "api/dashboard-analytics/",
    views_dashboard.dashboard_analytics_api,
    name="dashboard_analytics_api",
),

path(
    "api/dashboard-mapping/",
    views_dashboard.dashboard_mapping_api,
    name="dashboard_mapping_api",
),

path(
    "api/dashboard-score/",
    views_dashboard.dashboard_score_api,
    name="dashboard_score_api",
),

# ============================================================
# END urlpatterns
# ============================================================
# ============================================================
# MASTER UPLOAD
# ============================================================

path(
    "upload/",
    views_upload.upload_home,
    name="upload_home",
),

path(
    "upload/master/",
    views_upload.upload_master_template,
    name="upload_master_template",
),

path(
    "upload/status/",
    views_upload.import_status,
    name="import_status",
),

path(
    "download/master-template/",
    views_upload.download_master_template,
    name="download_master_template",
),
path("reports/", views_reports.reports_home, name="reports_home"),
    path("reports/institution/<int:institution_id>/", views_reports.institution_report, name="institution_report"),
    path("reports/school/<int:school_id>/", views_reports.school_report, name="school_report"),
    path("reports/department/<int:department_id>/", views_reports.department_report, name="department_report"),
    
    # AI Generation APIs
    path("api/generate-ai-report/", views_reports.generate_ai_report_api, name="generate_ai_report_api"),
    path("api/naac-analysis/", views_reports.naac_analysis_api, name="naac_analysis_api"),

    # ============================================================
    # MASTER UPLOAD
    # ============================================================
    path("upload/", views_upload.upload_home, name="upload_home"),
    path("upload/master/", views_upload.upload_master_template, name="upload_master_template"),
    path("upload/status/", views_upload.import_status, name="import_status"),
    path("download/master-template/", views_upload.download_master_template, name="download_master_template"),
    path("api/generate-ai-report/", views_reports.generate_ai_report_api, name="generate_ai_report_api"),
    # Add inside urlpatterns list in intelligence/urls.py

    path("api/command-data-filter/", views_reports.get_filtered_command_data_api, name="get_filtered_command_data_api"),
    path("api/download-accreditation-report/", views_reports.generate_accreditation_report_download_api, name="generate_accreditation_report_download_api"),
    path(
        "api/naac-nba-recommendations/",
        views_reports.get_naac_nba_recommendations_api,
        name="get_naac_nba_recommendations_api"
    ),
    path(
        "api/command-data-filter/",
        views_reports.get_filtered_command_data_api,
        name="get_filtered_command_data_api"
    ),
    path(
        "api/download-accreditation-report/",
        views_reports.generate_accreditation_report_download_api,
        name="generate_accreditation_report_download_api"
    ),
    path("upload/master/", views_upload.upload_master_template, name="upload_master_template"),
    path("download/master-template/", views_upload.download_master_template, name="download_master_template"),
    path("api/Strength-overview/", views_dashboard.health_overview_api, name="health_overview_api"),
    path("api/dashboard-analytics/", views_dashboard.dashboard_analytics_api, name="dashboard_analytics_api"),
]