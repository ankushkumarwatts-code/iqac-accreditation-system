from dashboard.models import Institution, School, Department, Faculty, Student
from intelligence.models import DepartmentHealth, SchoolHealth, InstitutionHealth


def run():

    # =========================
    # INSTITUTION
    # =========================

    inst = Institution.objects.create(
        name="ABC University",
        established_year=2005,
        naac_grade="A++",
        affiliated_university="Self",
        vision="Excellence in Education",
        mission="Innovation and Research"
    )

    inst_health = InstitutionHealth.objects.create(
        institution=inst
    )

    # =========================
    # SCHOOLS
    # =========================

    schools = []

    for i in range(1, 4):
        school = School.objects.create(
            name=f"School {i}",
            institution=inst
        )

        SchoolHealth.objects.create(school=school)

        schools.append(school)

    # =========================
    # DEPARTMENTS
    # =========================

    departments = []

    for s in schools:
        for j in range(1, 4):
            dept = Department.objects.create(
                name=f"{s.name} - Dept {j}",
                school=s,
                established_year=2010,
                intake=60
            )

            DepartmentHealth.objects.create(
                department=dept,
                health_score=50 + j * 10,
                status="Moderate"
            )

            departments.append(dept)

    # =========================
    # FACULTY
    # =========================

    for dept in departments:
        for k in range(5):

            Faculty.objects.create(
                name=f"{dept.name} Faculty {k}",
                department=dept,
                qualification="PhD",
                is_phd=True if k % 2 == 0 else False,
                experience_years=5 + k,
                research_publications=2 * k,
                patents=k,
                funded_projects=1,
                api_score=60 + k
            )

    # =========================
    # STUDENTS
    # =========================

    for dept in departments:
        for s in range(20):

            Student.objects.create(
                name=f"{dept.name} Student {s}",
                department=dept,
                year_of_admission=2022,
                current_year=3,
                cgpa=6 + (s % 4),
                placed=True if s % 3 == 0 else False
            )

    print("✅ Dummy Data Created Successfully")