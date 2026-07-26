from intelligence.models import (
    DepartmentHealth,
    SchoolHealth,
)

from dashboard.models import (
    Department,
    School,
    Faculty,
    Student,
)


class RankingEngine:

    # ==========================================
    # Department Ranking
    # ==========================================

    def department_rankings(self, profile=None):

        departments = Department.objects.select_related(
            "school"
        )

        if profile:

            role = profile.role

            if role in [
                "school_dean",
                "school_principal",
            ]:
                departments = departments.filter(
                    school=profile.school
                )

            elif role == "hod":

                departments = departments.filter(
                    school=profile.department.school
                )

            elif role == "faculty":

                departments = departments.filter(
                    id=profile.department.id
                )

        ranking = []

        for dept in departments:

            health = DepartmentHealth.objects.filter(
                department=dept
            ).first()

            score = 0

            if health:
                score = health.health_score

            ranking.append({

                "department": dept,

                "school": dept.school,

                "score": score,

                "status": health.status if health else "N/A",

            })

        ranking.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        for index, row in enumerate(ranking):

            row["rank"] = index + 1

        return ranking

    # ==========================================
    # School Ranking
    # ==========================================

    def school_rankings(self):

        ranking = []

        for school in School.objects.all():

            health = SchoolHealth.objects.filter(
                school=school
            ).first()

            ranking.append({

                "school": school,

                "score": health.health_score if health else 0

            })

        ranking.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        for index, row in enumerate(ranking):

            row["rank"] = index + 1

        return ranking

    # ==========================================
    # Faculty Ranking
    # ==========================================

    def faculty_rankings(self):

        faculty = Faculty.objects.all().order_by(
            "-api_score"
        )

        ranking = []

        for index, person in enumerate(faculty):

            ranking.append({

                "rank": index + 1,

                "faculty": person,

                "department": person.department,

                "api_score": person.api_score,

                "research": person.research_publications,

                "patents": person.patents,

                "projects": person.funded_projects,

            })

        return ranking

    # ==========================================
    # Student Ranking
    # ==========================================

    def student_rankings(self):

        students = Student.objects.all().order_by(
            "-cgpa"
        )

        ranking = []

        for index, student in enumerate(students):

            ranking.append({

                "rank": index + 1,

                "student": student,

                "department": student.department,

                "cgpa": student.cgpa,

                "placed": student.placed,

            })

        return ranking

    # ==========================================
    # Top Departments
    # ==========================================

    def top_departments(self, limit=5):

        return self.department_rankings()[:limit]

    # ==========================================
    # Bottom Departments
    # ==========================================

    def bottom_departments(self, limit=5):

        return self.department_rankings()[-limit:]

    # ==========================================
    # Top Schools
    # ==========================================

    def top_schools(self, limit=5):

        return self.school_rankings()[:limit]

    # ==========================================
    # Bottom Schools
    # ==========================================

    def bottom_schools(self, limit=5):

        return self.school_rankings()[-limit:]
        # ==========================================
    # Institution Ranking
    # ==========================================

    def institution_ranking(self):

        return [{
            "institution": "All Institutions",
            "score": 0,
            "rank": 1,
        }]

    # ==========================================
    # School Ranking (Compatibility)
    # ==========================================

    def school_ranking(self):

        return self.school_rankings()

    # ==========================================
    # Department Ranking (Compatibility)
    # ==========================================

    def department_ranking(self, profile=None):

        return self.department_rankings(profile)
        # ==========================================
    # Compatibility Methods
    # ==========================================

    def school_ranking_all(self):
        return self.school_rankings()

    def department_ranking_all(self, profile=None):
        return self.department_rankings(profile)

    def faculty_ranking_all(self):
        return self.faculty_rankings()

    def student_ranking_all(self):
        return self.student_rankings()
    # ==========================================================
# Compatibility API
# ==========================================================

def institution_ranking(self):
    return [{
        "rank": 1,
        "institution": "System",
        "score": 0,
    }]

def school_ranking(self, institution=None):
    return self.school_rankings()

def school_ranking_all(self):
    return self.school_rankings()

def department_ranking(self, institution=None):
    return self.department_rankings()

def department_ranking_all(self):
    return self.department_rankings()

def faculty_ranking(self, institution=None):
    return self.faculty_rankings()

def student_ranking(self, institution=None):
    return self.student_rankings()

def department_ranking_school(self, school):
    return [
        x for x in self.department_rankings()
        if x["school"] == school
    ]

def faculty_ranking_school(self, school):
    return [
        x for x in self.faculty_rankings()
        if x["department"].school == school
    ]

def student_ranking_school(self, school):
    return [
        x for x in self.student_rankings()
        if x["department"].school == school
    ]

def faculty_ranking_department(self, department):
    return [
        x for x in self.faculty_rankings()
        if x["department"] == department
    ]

def student_ranking_department(self, department):
    return [
        x for x in self.student_rankings()
        if x["department"] == department
    ]