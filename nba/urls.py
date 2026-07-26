from django.urls import path
from .views import nba_dashboard, upload_nba_metric, download_nba_template

urlpatterns = [
    path('dashboard/', nba_dashboard, name='nba_dashboard'),
    path('upload-nba/', upload_nba_metric, name='upload_nba_metric'),
    path('download-template/<int:metric_id>/', download_nba_template, name='download_nba_template'),
]