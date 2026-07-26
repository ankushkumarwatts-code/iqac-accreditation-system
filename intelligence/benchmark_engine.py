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
)


class BenchmarkEngine:

    # ======================================================
    # Institution Benchmark
    # ======================================================

    def institution_summary(self):

        institutions = Institution.objects.all()

        summary = []

        for institution in institutions:

            health = InstitutionHealth.objects.filter(
                institution=institution
            ).first()

            summary.append({

                "institution": institution,

                "health_score": health.health_score if health else 0,

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

            })

        return summary

    # ======================================================
    # School Benchmark
    # ======================================================

    def school_summary(self):

        schools = School.objects.all()

        summary = []

        for school in schools:

            health = SchoolHealth.objects.filter(
                school=school
            ).first()

            summary.append({

                "school": school,

                "health_score": health.health_score if health else 0,

                "departments": school.departments.count(),

                "faculty": Faculty.objects.filter(
                    department__school=school
                ).count(),

                "students": Student.objects.filter(
                    department__school=school
                ).count(),

            })

        return summary

    # ======================================================
    # Department Benchmark
    # ======================================================

    def department_summary(self, profile=None):

        departments = Department.objects.select_related(
            "school"
        )

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

        summary = []

        for dept in departments:

            health = DepartmentHealth.objects.filter(
                department=dept
            ).first()

            summary.append({

                "department": dept,

                "school": dept.school,

                "health_score": health.health_score if health else 0,

                "naac_score": health.naac_score if health else 0,

                "nba_score": health.nba_score if health else 0,

                "status": health.status if health else "N/A",

                "faculty": dept.faculty.count(),

                "students": dept.students.count(),

                "programs": dept.programs.count(),

            })

        return summary

    # ======================================================
    # Top Departments
    # ======================================================

    def top_departments(self, limit=5):

        departments = sorted(

            self.department_summary(),

            key=lambda x: x["health_score"],

            reverse=True,

        )

        return departments[:limit]

    # ======================================================
    # Bottom Departments
    # ======================================================

    def bottom_departments(self, limit=5):

        departments = sorted(

            self.department_summary(),

            key=lambda x: x["health_score"]

        )

        return departments[:limit]

    # ======================================================
    # Top Schools
    # ======================================================

    def top_schools(self, limit=5):

        schools = sorted(

            self.school_summary(),

            key=lambda x: x["health_score"],

            reverse=True,

        )

        return schools[:limit]

    # ======================================================
    # Bottom Schools
    # ======================================================

    def bottom_schools(self, limit=5):

        schools = sorted(

            self.school_summary(),

            key=lambda x: x["health_score"]

        )

        return schools[:limit]

    # ======================================================
    # Overall Benchmark
    # ======================================================

    def overall_summary(self):

        return {

            "institutions": self.institution_summary(),

            "schools": self.school_summary(),

            "departments": self.department_summary(),

            "top_departments": self.top_departments(),

            "top_schools": self.top_schools(),

        }
        # ======================================================
    # System Dashboard
    # ======================================================

    def system_dashboard(self):

        return self.overall_summary()

    # ======================================================
    # Institution Dashboard
    # ======================================================

    def institution_dashboard(self, institution):

        return {
            "institution": institution,
            "summary": [
                x for x in self.institution_summary()
                if x["institution"] == institution
            ]
        }

    # ======================================================
    # School Dashboard
    # ======================================================

    def school_dashboard(self, school):

        return {
            "school": school,
            "summary": [
                x for x in self.school_summary()
                if x["school"] == school
            ]
        }

    # ======================================================
    # Department Dashboard
    # ======================================================

    def department_dashboard(self, department):

        return {
            "department": department,
            "summary": [
                x for x in self.department_summary()
                if x["department"] == department
            ]
        }