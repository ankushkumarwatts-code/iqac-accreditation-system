from statistics import mean

from dashboard.models import Faculty, Student
from .models import (
    DepartmentHealth,
    SchoolHealth,
    InstitutionHealth,
)


class ScoringEngine:

    def __init__(self):
        pass

    # =====================================================
    # Department Score
    # =====================================================

    def department_score(self, department):

        health = DepartmentHealth.objects.filter(
            department=department
        ).first()

        faculty = Faculty.objects.filter(
            department=department
        )

        students = Student.objects.filter(
            department=department
        )

        faculty_api = mean(
            [f.api_score for f in faculty]
        ) if faculty.exists() else 0

        student_cgpa = mean(
            [s.cgpa for s in students]
        ) if students.exists() else 0

        placement = 0

        if students.exists():

            placement = (
                students.filter(
                    placed=True
                ).count() / students.count()
            ) * 100

        health_score = health.health_score if health else 0

        overall = round(

            (
                health_score * 0.40
                + faculty_api * 0.20
                + student_cgpa * 0.20
                + placement * 0.20
            ),

            2,

        )

        return {

            "health_score": health_score,

            "faculty_score": round(faculty_api, 2),

            "student_score": round(student_cgpa, 2),

            "placement_score": round(placement, 2),

            "overall_score": overall,

        }

    # =====================================================
    # School Score
    # =====================================================

    def school_score(self, school):

        health = SchoolHealth.objects.filter(
            school=school
        ).first()

        departments = school.departments.all()

        scores = []

        for dept in departments:

            scores.append(
                self.department_score(dept)["overall_score"]
            )

        return {

            "health_score": health.health_score if health else 0,

            "overall_score": round(
                mean(scores), 2
            ) if scores else 0,

        }

    # =====================================================
    # Institution Score
    # =====================================================

    def institution_score(self, institution):

        health = InstitutionHealth.objects.filter(
            institution=institution
        ).first()

        schools = institution.schools.all()

        scores = []

        for school in schools:

            scores.append(
                self.school_score(school)["overall_score"]
            )

        return {

            "health_score": health.health_score if health else 0,

            "overall_score": round(
                mean(scores), 2
            ) if scores else 0,

        }

    # =====================================================
    # Faculty Score
    # =====================================================

    def faculty_score(self, faculty):

        return {

            "api_score": faculty.api_score,

            "research_publications": faculty.research_publications,

            "patents": faculty.patents,

            "funded_projects": faculty.funded_projects,

        }

    # =====================================================
    # Student Score
    # =====================================================

    def student_score(self, student):

        return {

            "cgpa": student.cgpa,

            "placed": student.placed,

        }