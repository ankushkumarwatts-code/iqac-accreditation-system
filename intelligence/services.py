from django.db.models import Avg, Count, Sum, Q
from django.utils import timezone

from dashboard.models import (
    Institution,
    School,
    Department,
    Faculty,
    Student,
    UserProfile,
    GovernanceRole,
    FacultyPerformanceScore,
)

from intelligence.models import (
    InstitutionHealth,
    SchoolHealth,
    DepartmentHealth,
    DepartmentRisk,
)

from intelligence.analytics import AnalyticsEngine
from intelligence.ranking_engine import RankingEngine
from intelligence.kpi_engine import KPIEngine
from intelligence.benchmark_engine import BenchmarkEngine
from intelligence.risk_engine import RiskEngine
from intelligence.ai_engine import AIEngine
from intelligence.mapping_engine import MappingEngine
from intelligence.scoring_engine import ScoringEngine


analytics_engine = AnalyticsEngine()

ranking_engine = RankingEngine()

kpi_engine = KPIEngine()

benchmark_engine = BenchmarkEngine()

risk_engine = RiskEngine()

ai_engine = AIEngine()

mapping_engine = MappingEngine()

scoring_engine = ScoringEngine()


# ============================================================
# Dashboard Service
# ============================================================

class DashboardService:

    """
    Institutional Brain
    Dashboard Business Service
    """

    def __init__(self):

        self.analytics = analytics_engine

        self.ranking = ranking_engine

        self.kpi = kpi_engine

        self.benchmark = benchmark_engine

        self.risk = risk_engine

        self.ai = ai_engine

        self.mapping = mapping_engine

        self.scoring = scoring_engine

    # =========================================================
    # User Profile
    # =========================================================

    def user_profile(self, user):

        return UserProfile.objects.filter(

            user=user

        ).select_related(

            "institution",

            "school",

            "department"

        ).first()

    # =========================================================
    # User Scope
    # =========================================================

    def user_scope(self, profile):

        if profile is None:

            return "SYSTEM"

        if profile.department:

            return "DEPARTMENT"

        if profile.school:

            return "SCHOOL"

        if profile.institution:

            return "INSTITUTION"

        return "SYSTEM"

    # =========================================================
    # Dashboard Cards
    # =========================================================

    def dashboard_cards(self, scope, profile):

        cards = {}

        if scope == "INSTITUTION":

            institution = profile.institution

            cards = {

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

        elif scope == "SCHOOL":

            school = profile.school

            cards = {

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

        elif scope == "DEPARTMENT":

            department = profile.department

            cards = {

                "faculty":

                    Faculty.objects.filter(

                        department=department

                    ).count(),

                "students":

                    Student.objects.filter(

                        department=department

                    ).count(),

            }

        else:

            cards = {

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

            }

        return cards

    # =========================================================
    # CONTINUED IN PART-2
    # =========================================================
        # =========================================================
    # KPI Service
    # =========================================================

    def dashboard_kpi(self, scope, profile):

        if scope == "INSTITUTION":

            return self.kpi.institution_dashboard(

                profile.institution

            )

        elif scope == "SCHOOL":

            return self.kpi.school_dashboard(

                profile.school

            )

        elif scope == "DEPARTMENT":

            return self.kpi.department_dashboard(

                profile.department

            )

        return self.kpi.system_dashboard()

    # =========================================================
    # Analytics Service
    # =========================================================

    def dashboard_analytics(self, scope, profile):

        if scope == "INSTITUTION":

            return self.analytics.institution_dashboard(

                profile.institution

            )

        elif scope == "SCHOOL":

            return self.analytics.school_dashboard(

                profile.school

            )

        elif scope == "DEPARTMENT":

            return self.analytics.department_dashboard(

                profile.department

            )

        return self.analytics.system_dashboard()

    # =========================================================
    # Ranking Service
    # =========================================================

    def dashboard_rankings(self, scope, profile):

        rankings = {

            "institution": [],

            "school": [],

            "department": [],

            "faculty": [],

            "student": [],

        }

        if scope == "INSTITUTION":

            institution = profile.institution

            rankings["school"] = self.ranking.school_ranking(

                institution

            )

            rankings["department"] = self.ranking.department_ranking(

                institution

            )

            rankings["faculty"] = self.ranking.faculty_ranking(

                institution

            )

            rankings["student"] = self.ranking.student_ranking(

                institution

            )

        elif scope == "SCHOOL":

            school = profile.school

            rankings["department"] = self.ranking.department_ranking_school(

                school

            )

            rankings["faculty"] = self.ranking.faculty_ranking_school(

                school

            )

            rankings["student"] = self.ranking.student_ranking_school(

                school

            )

        elif scope == "DEPARTMENT":

            department = profile.department

            rankings["faculty"] = self.ranking.faculty_ranking_department(

                department

            )

            rankings["student"] = self.ranking.student_ranking_department(

                department

            )

        else:

            rankings["institution"] = self.ranking.institution_ranking()

            rankings["school"] = self.ranking.school_ranking_all()

            rankings["department"] = self.ranking.department_ranking_all()

        return rankings

    # =========================================================
    # Benchmark Service
    # =========================================================

    def dashboard_benchmark(self, scope, profile):

        if scope == "INSTITUTION":

            return self.benchmark.institution_dashboard(

                profile.institution

            )

        elif scope == "SCHOOL":

            return self.benchmark.school_dashboard(

                profile.school

            )

        elif scope == "DEPARTMENT":

            return self.benchmark.department_dashboard(

                profile.department

            )

        return self.benchmark.system_dashboard()

    # =========================================================
    # CONTINUED IN PART-3
    # =========================================================
        # =========================================================
    # Risk Service
    # =========================================================

    def dashboard_risk(self, scope, profile):

        if scope == "INSTITUTION":

            return self.risk.institution_dashboard(

                profile.institution

            )

        elif scope == "SCHOOL":

            return self.risk.school_dashboard(

                profile.school

            )

        elif scope == "DEPARTMENT":

            return self.risk.department_dashboard(

                profile.department

            )

        return self.risk.system_dashboard()

    # =========================================================
    # AI Recommendation Service
    # =========================================================

    def dashboard_ai(self, scope, profile):

        if scope == "INSTITUTION":

            return self.ai.institution_dashboard(

                profile.institution

            )

        elif scope == "SCHOOL":

            return self.ai.school_dashboard(

                profile.school

            )

        elif scope == "DEPARTMENT":

            return self.ai.department_dashboard(

                profile.department

            )

        return self.ai.system_dashboard()

    # =========================================================
    # Mapping Service
    # =========================================================

    def dashboard_mapping(self, scope, profile):

        if scope == "INSTITUTION":

            return self.mapping.complete_institution_graph(

                profile.institution

            )

        elif scope == "SCHOOL":

            return self.mapping.complete_school_graph(

                profile.school

            )

        elif scope == "DEPARTMENT":

            return self.mapping.complete_department_graph(

                profile.department

            )

        return None

    # =========================================================
    # Scoring Service
    # =========================================================

    def dashboard_scores(self, scope, profile):

        if scope == "INSTITUTION":

            return self.scoring.institution_score(

                profile.institution

            )

        elif scope == "SCHOOL":

            return self.scoring.school_score(

                profile.school

            )

        elif scope == "DEPARTMENT":

            return self.scoring.department_score(

                profile.department

            )

        return None

    # =========================================================
    # Dashboard Context
    # =========================================================

    def dashboard_context(self, user):

        profile = self.user_profile(user)

        scope = self.user_scope(profile)

        context = {

            "profile": profile,

            "scope": scope,

            "cards":
                self.dashboard_cards(
                    scope,
                    profile
                ),

            "analytics":
                self.dashboard_analytics(
                    scope,
                    profile
                ),

            "rankings":
                self.dashboard_rankings(
                    scope,
                    profile
                ),

            "kpi":
                self.dashboard_kpi(
                    scope,
                    profile
                ),

            "benchmark":
                self.dashboard_benchmark(
                    scope,
                    profile
                ),

            "risk":
                self.dashboard_risk(
                    scope,
                    profile
                ),

            "ai":
                self.dashboard_ai(
                    scope,
                    profile
                ),

            "mapping":
                self.dashboard_mapping(
                    scope,
                    profile
                ),

            "scores":
                self.dashboard_scores(
                    scope,
                    profile
                ),

            "generated_on":
                timezone.now(),

        }

        return context

    # =========================================================
    # CONTINUED IN PART-4
    # =========================================================
        # =========================================================
    # Institution Service
    # =========================================================

    def institution_context(self, institution):

        return {

            "institution": institution,

            "mapping":
                self.mapping.complete_institution_graph(
                    institution
                ),

            "analytics":
                self.analytics.institution_dashboard(
                    institution
                ),

            "ranking":
                self.ranking.institution_ranking(),

            "benchmark":
                self.benchmark.institution_dashboard(
                    institution
                ),

            "risk":
                self.risk.institution_dashboard(
                    institution
                ),

            "ai":
                self.ai.institution_dashboard(
                    institution
                ),

            "score":
                self.scoring.institution_score(
                    institution
                ),

            "generated_on":
                timezone.now(),

        }

    # =========================================================
    # School Service
    # =========================================================

    def school_context(self, school):

        return {

            "school": school,

            "mapping":
                self.mapping.complete_school_graph(
                    school
                ),

            "analytics":
                self.analytics.school_dashboard(
                    school
                ),

            "benchmark":
                self.benchmark.school_dashboard(
                    school
                ),

            "risk":
                self.risk.school_dashboard(
                    school
                ),

            "ai":
                self.ai.school_dashboard(
                    school
                ),

            "score":
                self.scoring.school_score(
                    school
                ),

            "generated_on":
                timezone.now(),

        }

    # =========================================================
    # Department Service
    # =========================================================

    def department_context(self, department):

        return {

            "department": department,

            "mapping":
                self.mapping.complete_department_graph(
                    department
                ),

            "analytics":
                self.analytics.department_dashboard(
                    department
                ),

            "benchmark":
                self.benchmark.department_dashboard(
                    department
                ),

            "risk":
                self.risk.department_dashboard(
                    department
                ),

            "ai":
                self.ai.department_dashboard(
                    department
                ),

            "score":
                self.scoring.department_score(
                    department
                ),

            "generated_on":
                timezone.now(),

        }

    # =========================================================
    # Health Service
    # =========================================================

    def health_summary(self):

        return {

            "institutions":
                InstitutionHealth.objects.count(),

            "schools":
                SchoolHealth.objects.count(),

            "departments":
                DepartmentHealth.objects.count(),

            "healthy_departments":
                DepartmentHealth.objects.filter(
                    status="HEALTHY"
                ).count(),

            "critical_departments":
                DepartmentHealth.objects.filter(
                    status="CRITICAL"
                ).count(),

        }

    # =========================================================
    # Risk Service Summary
    # =========================================================

    def risk_summary(self):

        return {

            "total":
                DepartmentRisk.objects.count(),

            "critical":
                DepartmentRisk.objects.filter(
                    risk_level="CRITICAL"
                ).count(),

            "high":
                DepartmentRisk.objects.filter(
                    risk_level="HIGH"
                ).count(),

            "moderate":
                DepartmentRisk.objects.filter(
                    risk_level="MODERATE"
                ).count(),

            "low":
                DepartmentRisk.objects.filter(
                    risk_level="LOW"
                ).count(),

        }

    # =========================================================
    # CONTINUED IN PART-5
    # =========================================================
        # =========================================================
    # Faculty Summary Service
    # =========================================================

    def faculty_summary(self):

        return {

            "total_faculty":
                Faculty.objects.count(),

            "active_faculty":
                Faculty.objects.filter(
                    is_active=True
                ).count()
                if hasattr(Faculty, "is_active") else Faculty.objects.count(),

            "performance_records":
                FacultyPerformanceScore.objects.count(),

            "average_score":
                FacultyPerformanceScore.objects.aggregate(
                    Avg("overall_score")
                ).get("overall_score__avg", 0),

        }

    # =========================================================
    # Student Summary Service
    # =========================================================

    def student_summary(self):

        return {

            "total_students":
                Student.objects.count(),

            "active_students":
                Student.objects.filter(
                    is_active=True
                ).count()
                if hasattr(Student, "is_active") else Student.objects.count(),

        }

    # =========================================================
    # Governance Summary
    # =========================================================

    def governance_summary(self):

        return {

            "roles":
                GovernanceRole.objects.count(),

            "assigned_roles":
                GovernanceRole.objects.exclude(
                    faculty=None
                ).count()
                if hasattr(GovernanceRole, "faculty")
                else GovernanceRole.objects.count(),

        }

    # =========================================================
    # Institution Statistics
    # =========================================================

    def institution_statistics(self):

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

        }

    # =========================================================
    # Executive Dashboard Summary
    # =========================================================

    def executive_dashboard(self):

        return {

            "institution":
                self.institution_statistics(),

            "health":
                self.health_summary(),

            "risk":
                self.risk_summary(),

            "faculty":
                self.faculty_summary(),

            "students":
                self.student_summary(),

            "governance":
                self.governance_summary(),

            "generated_on":
                timezone.now(),

        }

    # =========================================================
    # CONTINUED IN PART-6
    # =========================================================
        # =========================================================
    # Performance Indicators
    # =========================================================

    def performance_summary(self):

        performance = FacultyPerformanceScore.objects.all()

        return {

            "records":
                performance.count(),

            "average_score":
                performance.aggregate(
                    Avg("overall_score")
                ).get("overall_score__avg", 0),

            "highest_score":
                performance.aggregate(
                    Sum("overall_score")
                ).get("overall_score__sum", 0),

        }

    # =========================================================
    # User Summary
    # =========================================================

    def user_summary(self):

        return {

            "registered_users":
                UserProfile.objects.count(),

            "institution_users":
                UserProfile.objects.filter(
                    institution__isnull=False
                ).count(),

            "school_users":
                UserProfile.objects.filter(
                    school__isnull=False
                ).count(),

            "department_users":
                UserProfile.objects.filter(
                    department__isnull=False
                ).count(),

        }

    # =========================================================
    # Dashboard Statistics
    # =========================================================

    def dashboard_statistics(self):

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

            "health_records":
                DepartmentHealth.objects.count(),

            "risk_records":
                DepartmentRisk.objects.count(),

        }

    # =========================================================
    # System Snapshot
    # =========================================================

    def system_snapshot(self):

        return {

            "statistics":
                self.dashboard_statistics(),

            "performance":
                self.performance_summary(),

            "users":
                self.user_summary(),

            "health":
                self.health_summary(),

            "risk":
                self.risk_summary(),

            "generated_on":
                timezone.now(),

        }

    # =========================================================
    # Export Dashboard
    # =========================================================

    def export_dashboard(self, user):

        profile = self.user_profile(user)

        scope = self.user_scope(profile)

        return {

            "context":
                self.dashboard_context(user),

            "snapshot":
                self.system_snapshot(),

            "scope":
                scope,

            "exported_on":
                timezone.now(),

        }

    # =========================================================
    # CONTINUED IN PART-7
    # =========================================================
        # =========================================================
    # System Health Report
    # =========================================================

    def system_health_report(self):

        return {

            "institution_health":

                InstitutionHealth.objects.count(),

            "school_health":

                SchoolHealth.objects.count(),

            "department_health":

                DepartmentHealth.objects.count(),

            "overall_health_score":

                DepartmentHealth.objects.aggregate(

                    Avg("health_score")

                ).get("health_score__avg", 0),

            "generated_on":

                timezone.now(),

        }

    # =========================================================
    # Institution Directory
    # =========================================================

    def institution_directory(self):

        return {

            "institutions":

                list(

                    Institution.objects.values(

                        "id",

                        "name"

                    )

                ),

            "schools":

                list(

                    School.objects.values(

                        "id",

                        "name",

                        "institution_id"

                    )

                ),

            "departments":

                list(

                    Department.objects.values(

                        "id",

                        "name",

                        "school_id"

                    )

                ),

        }

    # =========================================================
    # Quick Statistics
    # =========================================================

    def quick_statistics(self):

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

    # =========================================================
    # Executive Report
    # =========================================================

    def executive_report(self):

        return {

            "statistics":

                self.quick_statistics(),

            "health":

                self.system_health_report(),

            "performance":

                self.performance_summary(),

            "risk":

                self.risk_summary(),

            "generated_on":

                timezone.now(),

        }

    # =========================================================
    # System Report
    # =========================================================

    def system_report(self):

        return {

            "dashboard":

                self.executive_dashboard(),

            "snapshot":

                self.system_snapshot(),

            "executive":

                self.executive_report(),

            "directory":

                self.institution_directory(),

            "generated_on":

                timezone.now(),

        }

    # =========================================================
    # Engine Information
    # =========================================================

    def engine_information(self):

        return {

            "service":

                "Institutional Brain Dashboard Service",

            "version":

                "2.0",

            "author":

                "AK Innovations",

            "modules": [

                "Dashboard Service",

                "Analytics Service",

                "Ranking Service",

                "KPI Service",

                "Benchmark Service",

                "Risk Service",

                "AI Service",

                "Mapping Service",

                "Scoring Service",

                "Institution Service",

                "School Service",

                "Department Service",

                "Executive Dashboard",

                "System Report",

                "Export Dashboard",

            ],

        }

    # =========================================================
    # End of DashboardService
    # =========================================================