# =====================================
# MASTER TEMPLATE CONFIGURATION
# =====================================

REQUIRED_SHEETS = [

    "Institution",
    "Schools",
    "Departments",
    "Faculty",
    "Students",
    "Research Publications",
    "Patents",
    "Funded Projects",
    "Placements",
    "Activities",
    "Extension Activities",
    "Collaborations",
    "NAAC Metrics",
    "NBA Attainment",
    "NIRF Indicators",
]


# =====================================
# REQUIRED COLUMNS
# =====================================

SHEET_COLUMNS = {

    "Institution": [
        "Institution Name",
        "Established Year",
        "NAAC Grade",
        "University",
    ],

    "Schools": [
        "School Name",
        "Dean Name",
    ],

    "Departments": [
        "Department Name",
        "School",
        "Intake",
    ],

    "Faculty": [
        "Faculty Name",
        "Department",
        "Qualification",
        "Experience",
        "API Score",
    ],

    "Students": [
        "Student Name",
        "Department",
        "Admission Year",
        "Current Year",
        "CGPA",
    ],

    "Research Publications": [
        "Faculty Name",
        "Publication Title",
        "Journal",
        "Year",
    ],

    "Patents": [
        "Faculty Name",
        "Patent Title",
        "Year",
    ],

    "Funded Projects": [
        "Faculty Name",
        "Project Title",
        "Funding Agency",
        "Amount",
    ],

    "Placements": [
        "Student Name",
        "Department",
        "Company",
        "Package",
    ],

    "Activities": [
        "Activity Name",
        "Department",
        "Date",
    ],

    "Extension Activities": [
        "Activity Name",
        "Department",
        "Date",
    ],

    "Collaborations": [
        "Organization",
        "Type",
        "Start Date",
    ],

    "NAAC Metrics": [
        "Metric Code",
        "Metric Name",
        "Target Score",
        "Achieved Score",
    ],

    "NBA Attainment": [
        "Course Outcome",
        "Attainment",
    ],

    "NIRF Indicators": [
        "Category",
        "Indicator",
        "Current Value",
        "Target Value",
    ],
}