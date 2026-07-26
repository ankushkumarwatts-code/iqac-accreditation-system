from dashboard.models import (
    Institution,
    School,
    Department,
    Faculty,
    Student,
)

from intelligence.models import (
    DepartmentHealth,
    SchoolHealth,
    InstitutionHealth,
    DepartmentRisk,
)


class KPIEngine:

    # ======================================================
    # Executive KPI
    # ======================================================

    def executive_summary(self, profile=None):

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

        department_count = departments.count()

        faculty_count = Faculty.objects.filter(
            department__in=departments
        ).count()

        student_count = Student.objects.filter(
            department__in=departments
        ).count()

        health_records = DepartmentHealth.objects.filter(
            department__in=departments
        )

        risk_records = DepartmentRisk.objects.filter(
            department__in=departments
        )

        avg_health = 0

        if health_records.exists():

            avg_health = round(

                sum(
                    h.health_score
                    for h in health_records
                ) / health_records.count(),

                2

            )

        top_department = None

        if health_records.exists():

            top_department = max(
                health_records,
                key=lambda x: x.health_score
            )

        weak_departments = health_records.filter(
            health_score__lt=50
        ).count()

        moderate_departments = health_records.filter(
            health_score__gte=50,
            health_score__lt=75
        ).count()

        strong_departments = health_records.filter(
            health_score__gte=75
        ).count()

        high_risk = risk_records.filter(
            risk_level="HIGH"
        ).count()

        medium_risk = risk_records.filter(
            risk_level="MEDIUM"
        ).count()

        low_risk = risk_records.filter(
            risk_level="LOW"
        ).count()

        return {

            "institutions": Institution.objects.count(),

            "schools": School.objects.count(),

            "departments": department_count,

            "faculty": faculty_count,

            "students": student_count,

            "average_health": avg_health,

            "top_department": (
                top_department.department
                if top_department
                else None
            ),

            "top_department_score": (
                top_department.health_score
                if top_department
                else 0
            ),

            "strong_departments": strong_departments,

            "moderate_departments": moderate_departments,

            "weak_departments": weak_departments,

            "high_risk_departments": high_risk,

            "medium_risk_departments": medium_risk,

            "low_risk_departments": low_risk,

        }

    # ======================================================
    # Institution KPI
    # ======================================================

    def institution_kpi(self, institution):

        health = InstitutionHealth.objects.filter(
            institution=institution
        ).first()

        return {

            "institution": institution,

            "health_score": (
                health.health_score
                if health else 0
            ),

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

        }

    # ======================================================
    # School KPI
    # ======================================================

    def school_kpi(self, school):

        health = SchoolHealth.objects.filter(
            school=school
        ).first()

        return {

            "school": school,

            "health_score": (
                health.health_score
                if health else 0
            ),

            "departments": school.departments.count(),

            "faculty": Faculty.objects.filter(
                department__school=school
            ).count(),

            "students": Student.objects.filter(
                department__school=school
            ).count(),

        }

    # ======================================================
    # Department KPI
    # ======================================================

    def department_kpi(self, department):

        health = DepartmentHealth.objects.filter(
            department=department
        ).first()

        risk = DepartmentRisk.objects.filter(
            department=department
        ).first()

        return {

            "department": department,

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

            "status": (
                health.status
                if health else "N/A"
            ),

            "risk_level": (
                risk.risk_level
                if risk else "LOW"
            ),

            "faculty": department.faculty.count(),

            "students": department.students.count(),

            "programs": department.programs.count(),

        }

    # ======================================================
    # Dashboard Cards
    # ======================================================

    def dashboard_cards(self, profile=None):

        return self.executive_summary(profile)
        # ======================================================
    # System Dashboard
    # ======================================================

    def system_dashboard(self, profile=None):

        return {

            "cards": self.dashboard_cards(profile),

            "summary": self.executive_summary(profile),

        }
    # ======================================================
    # Compatibility Wrappers
    # ======================================================

    def institution_dashboard(self, institution):
        return self.institution_kpi(institution)


    def school_dashboard(self, school):
        return self.school_kpi(school)


    def department_dashboard(self, department):
        return self.department_kpi(department)