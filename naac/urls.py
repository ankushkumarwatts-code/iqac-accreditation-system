from django.urls import path
from .views import naac_dashboard, download_naac_template

urlpatterns = [
    path('dashboard/', naac_dashboard, name='naac_dashboard'),
    path('download-template/<int:metric_id>/', download_naac_template, name='download_naac_template'),
]