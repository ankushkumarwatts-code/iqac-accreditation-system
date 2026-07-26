from django.contrib import admin

from .models import (
    DepartmentHealth,
    SchoolHealth,
    InstitutionHealth,
    DepartmentRisk
)


# =====================================
# DEPARTMENT HEALTH ADMIN
# =====================================

@admin.register(DepartmentHealth)
class DepartmentHealthAdmin(admin.ModelAdmin):

    list_display = (
        "department",
        "health_score",
        "status",
    )

    search_fields = (
        "department__name",
    )

    list_filter = (
        "status",
    )

    ordering = ("-health_score",)


# =====================================
# SCHOOL HEALTH ADMIN
# =====================================

@admin.register(SchoolHealth)
class SchoolHealthAdmin(admin.ModelAdmin):

    list_display = (
        "school",
        "health_score",
    )

    search_fields = (
        "school__name",
    )

    ordering = ("-health_score",)


# =====================================
# INSTITUTION HEALTH ADMIN
# =====================================

@admin.register(InstitutionHealth)
class InstitutionHealthAdmin(admin.ModelAdmin):

    list_display = (
        "institution",
        "health_score",
    )

    search_fields = (
        "institution__name",
    )

    ordering = ("-health_score",)


# =====================================
# DEPARTMENT RISK ADMIN
# =====================================

@admin.register(DepartmentRisk)
class DepartmentRiskAdmin(admin.ModelAdmin):

    list_display = (
        "department",
        "nba_score",
        "naac_score",
        "risk_level",
        "issue",
        "created_at",
    )

    search_fields = (
        "department__name",
    )

    list_filter = (
        "risk_level",
    )

    ordering = ("-created_at",)