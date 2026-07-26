from django.urls import path

from .views import (
    upload_master_template,
    download_master_template,
)

from .history_views import (
    upload_history,
)

from .benchmark_views import (
    benchmark_dashboard,
)

from .ai_report_views import (
    ai_report_dashboard,
)

from .evidence_views import (
    evidence_repository,
)

from .activity_views import (
    activity_dashboard,
)

urlpatterns = [

    path(
        "upload-master-template/",
        upload_master_template,
        name="upload_master_template"
    ),

    path(
        "download-master-template/",
        download_master_template,
        name="download_master_template"
    ),

    path(
        "upload-history/",
        upload_history,
        name="upload_history"
    ),

    path(
        "benchmark-dashboard/",
        benchmark_dashboard,
        name="benchmark_dashboard"
    ),

    path(
        "ai-report-dashboard/",
        ai_report_dashboard,
        name="ai_report_dashboard"
    ),

    path(
        "evidence-repository/",
        evidence_repository,
        name="evidence_repository"
    ),

    path(
        "activity-dashboard/",
        activity_dashboard,
        name="activity_dashboard"
    ),
    
]