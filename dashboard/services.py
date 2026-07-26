"""
dashboard/services.py

Enterprise Service Layer
Institutional Brain

All dashboard business logic must live here.
Views should only call these services.

Version : 1.0
"""

from django.utils import timezone
from django.db.models import Count

from dashboard.models import (
    Institution,
    School,
    Department,
    Faculty,
    Student,
    UserProfile,
)

from intelligence.analytics import AnalyticsEngine
from intelligence.ranking_engine import RankingEngine
from intelligence.kpi_engine import KPIEngine
from intelligence.benchmark_engine import BenchmarkEngine
from intelligence.risk_engine import RiskEngine
from intelligence.ai_engine import AIEngine
from intelligence.mapping_engine import MappingEngine
from intelligence.scoring_engine import ScoringEngine

# ==========================================================
# Engine Initialization
# ==========================================================

analytics_engine = AnalyticsEngine()

ranking_engine = RankingEngine()

kpi_engine = KPIEngine()

benchmark_engine = BenchmarkEngine()

risk_engine = RiskEngine()

ai_engine = AIEngine()

mapping_engine = MappingEngine()

scoring_engine = ScoringEngine()


# ==========================================================
# User Scope Service
# ==========================================================

class UserScopeService:

    """
    Resolve current user profile and dashboard scope.
    """

    @staticmethod
    def get_profile(user):

        return (
            UserProfile.objects
            .select_related(
                "institution",
                "school",
                "department",
            )
            .filter(
                user=user
            )
            .first()
        )

    @staticmethod
    def get_scope(profile):

        if profile is None:
            return "SYSTEM"

        if profile.department:
            return "DEPARTMENT"

        if profile.school:
            return "SCHOOL"

        if profile.institution:
            return "INSTITUTION"

        return "SYSTEM"


# ==========================================================
# Dashboard Service
# ==========================================================

class DashboardService:

    """
    Complete Command Center Service
    """

    @staticmethod
    def command_center(user):

        profile = UserScopeService.get_profile(user)

        scope = UserScopeService.get_scope(profile)

        context = {

            "profile": profile,

            "scope": scope,

            "cards":
                kpi_engine.dashboard_cards(profile),

            "analytics":
                analytics_engine.executive_cards(profile),

            "ranking":
                ranking_engine.department_rankings(profile),

            "benchmark":
                benchmark_engine.department_summary(profile),

            "risk":
                risk_engine.summary(profile),

            "ai":
                ai_engine.executive_summary(profile),

            "generated_on":
                timezone.now(),

        }

        return context


# ==========================================================
# Dashboard Summary Service
# ==========================================================

class DashboardSummaryService:

    """
    Used by API
    """

    @staticmethod
    def summary(user):

        profile = UserScopeService.get_profile(user)

        return {

            "cards":
                kpi_engine.dashboard_cards(profile),

            "analytics":
                analytics_engine.executive_cards(profile),

            "risk":
                risk_engine.summary(profile),

            "generated":
                timezone.now(),

        }


# ==========================================================
# Dashboard Statistics Service
# ==========================================================

class DashboardStatisticsService:

    """
    Generic system statistics
    """

    @staticmethod
    def system_statistics():

        return {

            "institutions":
                Institution.objects.count(),

            "schools":
                School.objects.count(),

            "departments":
                Department.objects.count(),

            "faculty":
                Faculty.objects.count(),

            "students":
                Student.objects.count(),

            "users":
                UserProfile.objects.count(),

        }


# ==========================================================
# END OF PART-1
# ==========================================================
# ==========================================================
# Institution Service
# ==========================================================

class InstitutionService:

    """
    Institution Dashboard Service
    """

    @staticmethod
    def dashboard(institution):

        context = {

            "institution": institution,

            "mapping":
                mapping_engine.complete_institution_graph(
                    institution
                ),

            "analytics":
                analytics_engine.institution_overview(
                    institution
                ),

            "kpi":
                kpi_engine.institution_kpi(
                    institution
                ),

            "benchmark":
                benchmark_engine.institution_summary(),

            "risk":
                risk_engine.summary(),

            "score":
                scoring_engine.institution_score(
                    institution
                ),

            "generated_on":
                timezone.now(),

        }

        return context

    @staticmethod
    def api(institution):

        return {

            "mapping":
                mapping_engine.complete_institution_graph(
                    institution
                ),

            "analytics":
                analytics_engine.institution_overview(
                    institution
                ),

            "score":
                scoring_engine.institution_score(
                    institution
                ),

            "risk":
                risk_engine.summary(),

        }


# ==========================================================
# School Service
# ==========================================================

class SchoolService:

    """
    School Dashboard Service
    """

    @staticmethod
    def dashboard(school):

        context = {

            "school": school,

            "mapping":
                mapping_engine.complete_school_graph(
                    school
                ),

            "analytics":
                analytics_engine.school_overview(
                    school
                ),

            "kpi":
                kpi_engine.school_kpi(
                    school
                ),

            "benchmark":
                benchmark_engine.school_summary(),

            "risk":
                risk_engine.school_risk(
                    school
                ),

            "score":
                scoring_engine.school_score(
                    school
                ),

            "generated_on":
                timezone.now(),

        }

        return context

    @staticmethod
    def api(school):

        return {

            "mapping":
                mapping_engine.complete_school_graph(
                    school
                ),

            "analytics":
                analytics_engine.school_overview(
                    school
                ),

            "score":
                scoring_engine.school_score(
                    school
                ),

            "risk":
                risk_engine.school_risk(
                    school
                ),

        }


# ==========================================================
# Department Service
# ==========================================================

class DepartmentService:

    """
    Department Dashboard Service
    """

    @staticmethod
    def dashboard(department):

        context = {

            "department": department,

            "mapping":
                mapping_engine.complete_department_graph(
                    department
                ),

            "analytics":
                analytics_engine.department_overview(
                    department
                ),

            "kpi":
                kpi_engine.department_kpi(
                    department
                ),

            "benchmark":
                benchmark_engine.department_summary(),

            "risk":
                risk_engine.department_risk(
                    department
                ),

            "score":
                scoring_engine.department_score(
                    department
                ),

            "ai":
                ai_engine.department_recommendation(
                    department
                ),

            "generated_on":
                timezone.now(),

        }

        return context

    @staticmethod
    def api(department):

        return {

            "mapping":
                mapping_engine.complete_department_graph(
                    department
                ),

            "analytics":
                analytics_engine.department_overview(
                    department
                ),

            "score":
                scoring_engine.department_score(
                    department
                ),

            "risk":
                risk_engine.department_risk(
                    department
                ),

            "ai":
                ai_engine.department_recommendation(
                    department
                ),

        }


# ==========================================================
# Generic Entity Counter
# ==========================================================

class EntityCounterService:

    """
    Generic Counting Service
    """

    @staticmethod
    def institution_counts(institution):

        return {

            "schools":
                School.objects.filter(
                    institution=institution
                ).count(),

            "departments":
                Department.objects.filter(
                    school__institution=institution
                ).count(),

            "faculty":
                Faculty.objects.filter(
                    department__school__institution=institution
                ).count(),

            "students":
                Student.objects.filter(
                    department__school__institution=institution
                ).count(),

        }

    @staticmethod
    def school_counts(school):

        return {

            "departments":
                Department.objects.filter(
                    school=school
                ).count(),

            "faculty":
                Faculty.objects.filter(
                    department__school=school
                ).count(),

            "students":
                Student.objects.filter(
                    department__school=school
                ).count(),

        }

    @staticmethod
    def department_counts(department):

        return {

            "faculty":
                Faculty.objects.filter(
                    department=department
                ).count(),

            "students":
                Student.objects.filter(
                    department=department
                ).count(),

        }


# ==========================================================
# END OF PART-2
# ==========================================================
# ==========================================================
# Faculty Service
# ==========================================================

class FacultyService:

    """
    Faculty Operations
    """

    @staticmethod
    def profile(faculty):

        return {

            "faculty": faculty,

            "department": faculty.department,

            "school": faculty.department.school,

            "institution":
                faculty.department.school.institution,

            "score":
                scoring_engine.faculty_score(
                    faculty
                ),

        }

    @staticmethod
    def leaderboard():

        return ranking_engine.faculty_rankings()

    @staticmethod
    def total():

        return Faculty.objects.count()


# ==========================================================
# Student Service
# ==========================================================

class StudentService:

    """
    Student Operations
    """

    @staticmethod
    def profile(student):

        return {

            "student": student,

            "department": student.department,

            "school": student.department.school,

            "institution":
                student.department.school.institution,

            "score":
                scoring_engine.student_score(
                    student
                ),

        }

    @staticmethod
    def leaderboard():

        return ranking_engine.student_rankings()

    @staticmethod
    def total():

        return Student.objects.count()


# ==========================================================
# Executive Service
# ==========================================================

class ExecutiveService:

    """
    Dashboard Executive Summary
    """

    @staticmethod
    def overview(profile=None):

        return {

            "cards":
                kpi_engine.dashboard_cards(profile),

            "analytics":
                analytics_engine.executive_cards(profile),

            "benchmark":
                benchmark_engine.overall_summary(),

            "risk":
                risk_engine.summary(profile),

            "recommendations":
                ai_engine.executive_summary(profile),

            "health_distribution":
                analytics_engine.health_distribution(),

            "risk_distribution":
                analytics_engine.risk_distribution(),

        }


# ==========================================================
# Search Service
# ==========================================================

class SearchService:

    """
    Common Search Utilities
    """

    @staticmethod
    def institutions(keyword):

        return Institution.objects.filter(
            name__icontains=keyword
        ).values(
            "id",
            "name"
        )

    @staticmethod
    def schools(keyword):

        return School.objects.filter(
            name__icontains=keyword
        ).values(
            "id",
            "name"
        )

    @staticmethod
    def departments(keyword):

        return Department.objects.filter(
            name__icontains=keyword
        ).values(
            "id",
            "name"
        )

    @staticmethod
    def faculty(keyword):

        return Faculty.objects.filter(
            name__icontains=keyword
        ).values(
            "id",
            "name"
        )

    @staticmethod
    def students(keyword):

        return Student.objects.filter(
            name__icontains=keyword
        ).values(
            "id",
            "name"
        )


# ==========================================================
# Dashboard API Service
# ==========================================================

class DashboardAPIService:

    """
    All APIs will call this service.
    """

    @staticmethod
    def dashboard(user):

        return DashboardService.command_center(
            user
        )

    @staticmethod
    def summary(user):

        return DashboardSummaryService.summary(
            user
        )

    @staticmethod
    def executive(user):

        profile = UserScopeService.get_profile(
            user
        )

        return ExecutiveService.overview(
            profile
        )
# ==========================================================
# Health Service
# ==========================================================

class HealthService:

    """
    Health related operations.
    """

    @staticmethod
    def distribution():

        return analytics_engine.health_distribution()

    @staticmethod
    def institution(institution):

        return analytics_engine.institution_overview(
            institution
        )

    @staticmethod
    def school(school):

        return analytics_engine.school_overview(
            school
        )

    @staticmethod
    def department(department):

        return analytics_engine.department_overview(
            department
        )


# ==========================================================
# Risk Service
# ==========================================================

class RiskService:

    """
    Risk related operations.
    """

    @staticmethod
    def summary(profile=None):

        return risk_engine.summary(profile)

    @staticmethod
    def department(department):

        return risk_engine.department_risk(
            department
        )

    @staticmethod
    def alerts():

        return risk_engine.alerts()

    @staticmethod
    def distribution():

        return risk_engine.distribution()

    @staticmethod
    def critical():

        return risk_engine.critical_departments()

    @staticmethod
    def moderate():

        return risk_engine.moderate_departments()

    @staticmethod
    def low():

        return risk_engine.low_risk_departments()


# ==========================================================
# AI Recommendation Service
# ==========================================================

class RecommendationService:

    """
    AI Recommendation Wrapper.
    """

    @staticmethod
    def executive(profile=None):

        return ai_engine.executive_summary(
            profile
        )

    @staticmethod
    def department(department):

        return ai_engine.department_recommendation(
            department
        )

    @staticmethod
    def improvement_plan(department):

        return ai_engine.improvement_plan(
            department
        )


# ==========================================================
# Report Service
# ==========================================================

class ReportService:

    """
    Common dashboard reports.
    """

    @staticmethod
    def executive_report(user):

        return DashboardService.command_center(
            user
        )

    @staticmethod
    def institution_report(institution):

        return InstitutionService.dashboard(
            institution
        )

    @staticmethod
    def school_report(school):

        return SchoolService.dashboard(
            school
        )

    @staticmethod
    def department_report(department):

        return DepartmentService.dashboard(
            department
        )


# ==========================================================
# Export Service
# ==========================================================

class ExportService:

    """
    Export-ready dictionaries.
    """

    @staticmethod
    def institution(institution):

        return mapping_engine.export_mapping(
            institution
        )

    @staticmethod
    def json_graph(institution):

        return mapping_engine.json_graph(
            institution
        )

    @staticmethod
    def dashboard(institution):

        return mapping_engine.dashboard_response(
            institution
        )


# ==========================================================
# Cache Service
# ==========================================================

class CacheService:

    """
    Wrapper around MappingEngine cache.
    """

    @staticmethod
    def clear():

        return mapping_engine.clear_cache()

    @staticmethod
    def size():

        return mapping_engine.cache_size()


# ==========================================================
# System Service
# ==========================================================

class SystemService:

    """
    System level information.
    """

    @staticmethod
    def information():

        return {

            "generated_on":
                timezone.now(),

            "institutions":
                Institution.objects.count(),

            "schools":
                School.objects.count(),

            "departments":
                Department.objects.count(),

            "faculty":
                Faculty.objects.count(),

            "students":
                Student.objects.count(),

            "users":
                UserProfile.objects.count(),

            "engine":
                mapping_engine.engine_info(),

        }


# ==========================================================
# Service Registry
# ==========================================================

class ServiceRegistry:

    """
    Central access point for all services.
    """

    dashboard = DashboardService

    institution = InstitutionService

    school = SchoolService

    department = DepartmentService

    faculty = FacultyService

    student = StudentService

    executive = ExecutiveService

    statistics = DashboardStatisticsService

    summary = DashboardSummaryService

    search = SearchService

    risk = RiskService

    health = HealthService

    recommendation = RecommendationService

    report = ReportService

    export = ExportService

    cache = CacheService

    system = SystemService

# ==========================================================
# END OF SERVICES
# ==========================================================
