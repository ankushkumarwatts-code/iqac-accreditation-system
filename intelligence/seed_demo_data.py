from dashboard.models import Department, School, Institution
from intelligence.models import (
    DepartmentHealth,
    SchoolHealth,
    InstitutionHealth,
    DepartmentRisk
)

from naac.models import (
    NAACCriteria,
    NAACMetric,
    NAACMetricEntry
)

from nba.models import (
    NBACriteria
)

from django.contrib.auth.models import User


# =====================================
# DEMO USER
# =====================================

demo_user, _ = User.objects.get_or_create(
    username="admin"
)


# =====================================
# INSTITUTION
# =====================================

institution, _ = Institution.objects.get_or_create(
    name="Baba Farid Group of Institutions",
    defaults={
        "established_year": 1998
    }
)


# =====================================
# SCHOOLS
# =====================================

school_names = [

    "School Of Engineering",
    "School Of Sciences",
    "School Of Management",
    "School Of Agriculture",
    "School Of Humanities"

]

schools = {}

for name in school_names:

    school, _ = School.objects.get_or_create(
        name=name,
        defaults={
            "institution": institution
        }
    )

    schools[name] = school


# =====================================
# DEPARTMENTS
# =====================================

department_map = {

    "School Of Engineering": [

        "CSE",
        "ECE",
        "Mechanical",
        "Civil",
        "Electrical"

    ],

    "School Of Sciences": [

        "Physics",
        "Chemistry",
        "Mathematics"

    ],

    "School Of Management": [

        "MBA",
        "Commerce"

    ],

    "School Of Agriculture": [

        "Agriculture"

    ],

    "School Of Humanities": [

        "English",
        "Punjabi"

    ]
}


all_departments = []

for school_name, departments in department_map.items():

    school = schools[school_name]

    for dept_name in departments:

        dept, _ = Department.objects.get_or_create(
            name=dept_name,
            defaults={
                "school": school,
                "established_year": 2005
            }
        )

        all_departments.append(dept)


# =====================================
# PROFESSIONAL HEALTH SCORES
# =====================================

health_scores = {

    # EXCELLENT
    "CSE": (95, 92, 94),
    "Physics": (91, 89, 90),

    # VERY GOOD
    "ECE": (85, 83, 84),
    "Chemistry": (81, 79, 80),

    # GOOD
    "MBA": (76, 74, 75),
    "Agriculture": (73, 71, 72),
    "Electrical": (71, 69, 70),

    # AVERAGE
    "Commerce": (65, 63, 64),
    "Mathematics": (63, 61, 62),

    # WEAK
    "Mechanical": (57, 54, 55),
    "English": (53, 50, 51),

    # CRITICAL
    "Civil": (43, 40, 41),
    "Punjabi": (37, 34, 35)

}


# =====================================
# DEPARTMENT HEALTH
# =====================================

for dept in all_departments:

    naac, nba, health = health_scores.get(
        dept.name,
        (65, 60, 62)
    )

    DepartmentHealth.objects.update_or_create(
        department=dept,
        defaults={

            "naac_score": naac,
            "nba_score": nba,
            "health_score": health,

            "status":

            "EXCELLENT" if health >= 90 else

            "GOOD" if health >= 75 else

            "AVERAGE" if health >= 60 else

            "WEAK"

        }
    )


# =====================================
# RISK ANALYSIS
# =====================================

for dept in all_departments:

    if dept.name in ["Civil", "Punjabi"]:

        level = "HIGH"

    elif dept.name in ["Mechanical", "English"]:

        level = "MEDIUM"

    elif dept.name in ["Commerce", "Mathematics"]:

        level = "LOW"

    else:

        level = "LOW"

    DepartmentRisk.objects.update_or_create(
        department=dept,
        defaults={

            "risk_level": level,
            "naac_risk": level,
            "nba_risk": level

        }
    )


# =====================================
# SCHOOL HEALTH
# =====================================

school_scores = {

    "School Of Engineering": 68,
    "School Of Sciences": 86,
    "School Of Management": 72,
    "School Of Agriculture": 71,
    "School Of Humanities": 48

}

for school_name, score in school_scores.items():

    SchoolHealth.objects.update_or_create(
        school=schools[school_name],
        defaults={
            "health_score": score
        }
    )


# =====================================
# INSTITUTION HEALTH
# =====================================

InstitutionHealth.objects.update_or_create(
    institution=institution,
    defaults={
        "health_score": 70
    }
)


# =====================================
# NAAC CRITERIA
# =====================================

criteria_data = [

    ("1", "Curriculum"),
    ("2", "Teaching Learning"),
    ("3", "Research"),
    ("4", "Infrastructure"),
    ("5", "Student Support"),
    ("6", "Governance"),
    ("7", "Innovation")

]

for code, name in criteria_data:

    NAACCriteria.objects.get_or_create(
        code=code,
        defaults={
            "name": name
        }
    )


# =====================================
# METRICS
# =====================================

metric_data = [

    ("1", "1.1.1", "Curriculum Planning"),
    ("1", "1.2.1", "Academic Flexibility"),

    ("2", "2.1.1", "Student Enrollment"),
    ("2", "2.2.1", "Teaching Learning"),

    ("3", "3.1.1", "Research Facilities"),

    ("4", "4.1.1", "Infrastructure"),

    ("5", "5.1.1", "Student Support"),

    ("6", "6.1.1", "Governance"),

    ("7", "7.1.1", "Best Practices")

]



# =====================================
# METRIC PERFORMANCE
# =====================================

metric_scores = {

    "CSE": {

        "1.1.1": 96,
        "1.2.1": 94,
        "2.1.1": 92,
        "2.2.1": 95,
        "3.1.1": 91,
        "4.1.1": 94,
        "5.1.1": 90,
        "6.1.1": 88,
        "7.1.1": 93

    },

    "Physics": {

        "1.1.1": 91,
        "1.2.1": 89,
        "2.1.1": 88,
        "2.2.1": 90,
        "3.1.1": 94,
        "4.1.1": 91,
        "5.1.1": 87,
        "6.1.1": 85,
        "7.1.1": 89

    },

    "ECE": {

        "1.1.1": 84,
        "1.2.1": 82,
        "2.1.1": 80,
        "2.2.1": 85,
        "3.1.1": 76,
        "4.1.1": 83,
        "5.1.1": 81,
        "6.1.1": 79,
        "7.1.1": 82

    },

    "Chemistry": {

        "1.1.1": 82,
        "1.2.1": 80,
        "2.1.1": 78,
        "2.2.1": 79,
        "3.1.1": 86,
        "4.1.1": 82,
        "5.1.1": 79,
        "6.1.1": 76,
        "7.1.1": 78

    },

    "MBA": {

        "1.1.1": 76,
        "1.2.1": 74,
        "2.1.1": 72,
        "2.2.1": 78,
        "3.1.1": 69,
        "4.1.1": 75,
        "5.1.1": 76,
        "6.1.1": 73,
        "7.1.1": 74

    },

    "Agriculture": {

        "1.1.1": 74,
        "1.2.1": 72,
        "2.1.1": 70,
        "2.2.1": 71,
        "3.1.1": 68,
        "4.1.1": 76,
        "5.1.1": 72,
        "6.1.1": 70,
        "7.1.1": 71

    },

    "Electrical": {

        "1.1.1": 70,
        "1.2.1": 68,
        "2.1.1": 67,
        "2.2.1": 72,
        "3.1.1": 64,
        "4.1.1": 71,
        "5.1.1": 69,
        "6.1.1": 66,
        "7.1.1": 68

    },

    "Commerce": {

        "1.1.1": 66,
        "1.2.1": 64,
        "2.1.1": 63,
        "2.2.1": 64,
        "3.1.1": 59,
        "4.1.1": 68,
        "5.1.1": 64,
        "6.1.1": 60,
        "7.1.1": 62

    },

    "Mathematics": {

        "1.1.1": 64,
        "1.2.1": 62,
        "2.1.1": 60,
        "2.2.1": 58,
        "3.1.1": 70,
        "4.1.1": 63,
        "5.1.1": 61,
        "6.1.1": 59,
        "7.1.1": 60

    },

    "Mechanical": {

        "1.1.1": 58,
        "1.2.1": 55,
        "2.1.1": 52,
        "2.2.1": 54,
        "3.1.1": 46,
        "4.1.1": 60,
        "5.1.1": 53,
        "6.1.1": 50,
        "7.1.1": 52

    },

    "English": {

        "1.1.1": 54,
        "1.2.1": 51,
        "2.1.1": 48,
        "2.2.1": 49,
        "3.1.1": 44,
        "4.1.1": 56,
        "5.1.1": 50,
        "6.1.1": 47,
        "7.1.1": 48

    },

    "Civil": {

        "1.1.1": 42,
        "1.2.1": 40,
        "2.1.1": 38,
        "2.2.1": 35,
        "3.1.1": 30,
        "4.1.1": 44,
        "5.1.1": 38,
        "6.1.1": 34,
        "7.1.1": 36

    },

    "Punjabi": {

        "1.1.1": 36,
        "1.2.1": 34,
        "2.1.1": 32,
        "2.2.1": 29,
        "3.1.1": 26,
        "4.1.1": 40,
        "5.1.1": 33,
        "6.1.1": 30,
        "7.1.1": 31

    }

}


# =====================================
# CREATE METRICS
# =====================================

for c, code, desc in metric_data:

    criteria = NAACCriteria.objects.get(code=c)

    metric, _ = NAACMetric.objects.get_or_create(
        metric_code=code,
        criteria=criteria,
        defaults={
            "description": desc
        }
    )

    for dept in all_departments:

        dept_scores = metric_scores.get(
            dept.name,
            {}
        )

        achieved = dept_scores.get(
            code,
            65
        )

        NAACMetricEntry.objects.update_or_create(
            department=dept,
            metric=metric,
            defaults={

                "achieved_score": achieved,
                "target_score": 100,
                "year": 2025,
                "entered_by": demo_user

            }
        )


# =====================================
# NBA CRITERIA
# =====================================

nba_criteria = [

    "Criterion 1: Vision & Mission",
    "Criterion 2: Curriculum",
    "Criterion 3: Outcomes",
    "Criterion 4: Students",
    "Criterion 5: Faculty",
    "Criterion 6: Facilities",
    "Criterion 7: Continuous Improvement"

]

for name in nba_criteria:

    NBACriteria.objects.get_or_create(
        name=name
    )


print("🔥 PROFESSIONAL DEMO DATA ADDED SUCCESSFULLY 🔥")