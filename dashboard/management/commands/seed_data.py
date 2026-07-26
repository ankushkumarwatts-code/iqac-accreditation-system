from django.core.management.base import BaseCommand
from dashboard.models import *
import random


class Command(BaseCommand):
    help = "Seed dummy data"

    def handle(self, *args, **kwargs):

        # =========================
        # INSTITUTION
        # =========================
        inst = Institution.objects.create(
            name="ABC University",
            established_year=2000,
            vision="To be a global leader",
            mission="Quality education"
        )

        # =========================
        # SCHOOL
        # =========================
        school = School.objects.create(
            name="School of Engineering",
            institution=inst
        )

        # =========================
        # DEPARTMENTS
        # =========================
        dept_names = ["Computer Science", "Mechanical"]

        departments = []

        for name in dept_names:
            dept = Department.objects.create(
                name=name,
                school=school,
                established_year=2010,
                intake=120
            )
            departments.append(dept)

        # =========================
        # FACULTY
        # =========================
        for dept in departments:
            for i in range(3):
                Faculty.objects.create(
                    name=f"Dr {dept.name} Faculty {i+1}",
                    department=dept,
                    qualification="PhD",
                    is_phd=True,
                    experience_years=random.randint(2, 15),
                    research_publications=random.randint(1, 20),
                    patents=random.randint(0, 3),
                    funded_projects=random.randint(0, 5),
                    api_score=random.randint(50, 100)
                )

        # =========================
        # STUDENTS
        # =========================
        for dept in departments:

            faculty_list = list(dept.faculty.all())

            for i in range(10):
                Student.objects.create(
                    name=f"{dept.name} Student {i+1}",
                    department=dept,
                    year_of_admission=2022,
                    current_year=random.randint(1, 4),
                    cgpa=round(random.uniform(6.0, 9.5), 2),
                    placed=random.choice([True, False]),
                    mentor=random.choice(faculty_list)
                )

        self.stdout.write(self.style.SUCCESS("🔥 Dummy data created successfully!"))