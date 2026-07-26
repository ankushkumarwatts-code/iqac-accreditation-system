import pandas as pd

from dashboard.models import (
    Institution,
    School,
    Department,
    Faculty,
    Student
)


# =====================================
# IMPORT INSTITUTION
# =====================================

def import_institution(excel_file):

    df = pd.read_excel(
        excel_file,
        sheet_name="Institution"
    )

    for _, row in df.iterrows():

        Institution.objects.update_or_create(

            name=row["Institution Name"],

            defaults={

                "established_year": row["Established Year"],

                "naac_grade": row["NAAC Grade"],

                "affiliated_university": row["University"],

                "vision": "Institution Vision",

                "mission": "Institution Mission",
            }
        )


# =====================================
# IMPORT SCHOOLS
# =====================================

def import_schools(excel_file):

    df = pd.read_excel(
        excel_file,
        sheet_name="Schools"
    )

    institution = Institution.objects.first()

    for _, row in df.iterrows():

        School.objects.update_or_create(

            name=row["School Name"],

            defaults={
                "institution": institution,
                "dean_name": row["Dean Name"],
            }
        )


# =====================================
# IMPORT DEPARTMENTS
# =====================================

def import_departments(excel_file):

    df = pd.read_excel(
        excel_file,
        sheet_name="Departments"
    )

    for _, row in df.iterrows():

        school = School.objects.filter(
            name=row["School"]
        ).first()

        if school:

            Department.objects.update_or_create(

                name=row["Department Name"],

                defaults={
                    "school": school,
                    "intake": row["Intake"],
                    "established_year": 2000,
                }
            )


# =====================================
# IMPORT FACULTY
# =====================================

def import_faculty(excel_file):

    df = pd.read_excel(
        excel_file,
        sheet_name="Faculty"
    )

    for _, row in df.iterrows():

        department = Department.objects.filter(
            name=row["Department"]
        ).first()

        if department:

            Faculty.objects.update_or_create(

                name=row["Faculty Name"],

                defaults={

                    "department": department,

                    "qualification": row["Qualification"],

                    "experience_years": row["Experience"],

                    "api_score": row["API Score"],
                }
            )


# =====================================
# IMPORT STUDENTS
# =====================================

def import_students(excel_file):

    df = pd.read_excel(
        excel_file,
        sheet_name="Students"
    )

    for _, row in df.iterrows():

        department = Department.objects.filter(
            name=row["Department"]
        ).first()

        if department:

            Student.objects.update_or_create(

                name=row["Student Name"],

                defaults={

                    "department": department,

                    "year_of_admission": row["Admission Year"],

                    "current_year": row["Current Year"],

                    "cgpa": row["CGPA"],
                }
            )


# =====================================
# MASTER IMPORT
# =====================================

def import_master_template(excel_file):

    import_institution(excel_file)

    import_schools(excel_file)

    import_departments(excel_file)

    import_faculty(excel_file)

    import_students(excel_file)

    return True