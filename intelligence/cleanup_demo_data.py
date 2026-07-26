from dashboard.models import School, Department
from intelligence.models import (
    DepartmentHealth,
    SchoolHealth,
    DepartmentRisk
)

from naac.models import NAACMetricEntry



# =====================================
# REMOVE DEFAULT SCHOOL
# =====================================

School.objects.filter(
    name="Default School"
).delete()



# =====================================
# REMOVE DUPLICATE SCHOOLS
# =====================================

School.objects.filter(
    name="School OF Engineering"
).delete()



# =====================================
# REMOVE EXTRA DEPARTMENTS
# =====================================

extra_departments = [

    "DOPAMS",
    "Medical Department",
    "Mechanical Department",
    "CSE, IOT & AI",
    "Civil Engineering Department",
    "Electrical Department",
    "Agri Business Management",
    "Department of English",
    "Department Of Hindi",
    "Department Of Punjabi",
    "Department Of Social Science",
    "Department Of Fine Arts",
    "Department Of Humanities",
    "MBA Marketing",
    "MBA Finance",
    "MBA ( Human Resource Management)",
    "MBA ( Retail Management )",
    "BBA Department"

]



for dept_name in extra_departments:

    Department.objects.filter(
        name=dept_name
    ).delete()



print("🔥 DEMO CLEANUP COMPLETED 🔥")