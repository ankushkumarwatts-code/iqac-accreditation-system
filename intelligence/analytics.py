from intelligence.models import (
    DepartmentHealth,
    SchoolHealth,
    InstitutionHealth,
    DepartmentRisk,
)

from dashboard.models import (
    Institution,
    School,
    Department,
    Faculty,
    Student,
)


class AnalyticsEngine:

    # ======================================================
    # Executive Cards
    # ======================================================

    def executive_cards(self, profile=None):

        departments = Department.objects.all()

        if profile:

            if profile.role in [
                "school_dean",
                "school_principal",
            ]:

                departments = departments.filter(
                    school=profile.school
                )

            elif profile.role == "hod":

                departments = departments.filter(
                    school=profile.department.school
                )

            elif profile.role == "faculty":

                departments = departments.filter(
                    id=profile.department.id
                )

        health = DepartmentHealth.objects.filter(
            department__in=departments
        )

        avg_health = 0

        if health.exists():

            avg_health = round(

                sum(
                    h.health_score
                    for h in health
                ) / health.count(),

                2,

            )

        return {

            "institutions": Institution.objects.count(),

            "schools": School.objects.count(),

            "departments": departments.count(),

            "faculty": Faculty.objects.filter(
                department__in=departments
            ).count(),

            "students": Student.objects.filter(
                department__in=departments
            ).count(),

            "average_health": avg_health,

        }

    # ======================================================
    # Department Overview
    # ======================================================

    def department_overview(self, department):

        health = DepartmentHealth.objects.filter(
            department=department
        ).first()

        risk = DepartmentRisk.objects.filter(
            department=department
        ).first()

        return {

            "department": department,

            "faculty": department.faculty.count(),

            "students": department.students.count(),

            "programs": department.programs.count(),

            "health_score": (
                health.health_score
                if health else 0
            ),

            "naac_score": (
                health.naac_score
                if health else 0
            ),

            "nba_score": (
                health.nba_score
                if health else 0
            ),

            "risk_level": (
                risk.risk_level
                if risk else "LOW"
            ),

        }

    # ======================================================
    # School Overview
    # ======================================================

    def school_overview(self, school):

        health = SchoolHealth.objects.filter(
            school=school
        ).first()

        return {

            "school": school,

            "departments": school.departments.count(),

            "faculty": Faculty.objects.filter(
                department__school=school
            ).count(),

            "students": Student.objects.filter(
                department__school=school
            ).count(),

            "health_score": (
                health.health_score
                if health else 0
            ),

        }

    # ======================================================
    # Institution Overview
    # ======================================================

    def institution_overview(self, institution):

        health = InstitutionHealth.objects.filter(
            institution=institution
        ).first()

        return {

            "institution": institution,

            "schools": institution.schools.count(),

            "departments": Department.objects.filter(
                school__institution=institution
            ).count(),

            "faculty": Faculty.objects.filter(
                department__school__institution=institution
            ).count(),

            "students": Student.objects.filter(
                department__school__institution=institution
            ).count(),

            "health_score": (
                health.health_score
                if health else 0
            ),

        }

    # ======================================================
    # Health Distribution
    # ======================================================

    def health_distribution(self):

        return {

            "strong": DepartmentHealth.objects.filter(
                health_score__gte=75
            ).count(),

            "moderate": DepartmentHealth.objects.filter(
                health_score__gte=50,
                health_score__lt=75
            ).count(),

            "weak": DepartmentHealth.objects.filter(
                health_score__lt=50
            ).count(),

        }

    # ======================================================
    # Risk Distribution
    # ======================================================

    def risk_distribution(self):

        return {

            "high": DepartmentRisk.objects.filter(
                risk_level="HIGH"
            ).count(),

            "medium": DepartmentRisk.objects.filter(
                risk_level="MEDIUM"
            ).count(),

            "low": DepartmentRisk.objects.filter(
                risk_level="LOW"
            ).count(),

        }

    # ======================================================
    # Dashboard Charts
    # ======================================================

    def chart_data(self):

        return {

            "health": self.health_distribution(),

            "risk": self.risk_distribution(),

        }
    # ======================================================
    # System Dashboard
    # ======================================================

    def system_dashboard(self):

        return {

            "cards": self.executive_cards(),

            "charts": self.chart_data(),

            "health_distribution": self.health_distribution(),

            "risk_distribution": self.risk_distribution(),

        }
    # ======================================================
    # Institution Dashboard
    # ======================================================

    def institution_dashboard(self, institution):

        return {

            "overview": self.institution_overview(institution),

            "charts": self.chart_data(),

            "health_distribution": self.health_distribution(),

            "risk_distribution": self.risk_distribution(),

        }