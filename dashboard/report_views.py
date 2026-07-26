# ============================================================
# report_views.py
# Institutional Brain
# Part-1
# ============================================================

from django.contrib.auth.decorators import login_required

from intelligence.reports import (

    InstitutionPDFReport,
    SchoolPDFReport,
    DepartmentPDFReport,
    FacultyPDFReport,
    StudentPDFReport,

    InstitutionHealthPDFReport,
    SchoolHealthPDFReport,
    DepartmentHealthPDFReport,
    DepartmentRiskPDFReport,

    ExecutiveDashboardPDFReport,
    DashboardSummaryPDFReport,

    InstitutionExcelReport,
    SchoolExcelReport,
    DepartmentExcelReport,
    FacultyExcelReport,
    StudentExcelReport,

    InstitutionHealthExcelReport,
    SchoolHealthExcelReport,
    DepartmentHealthExcelReport,
    DepartmentRiskExcelReport,

    ExecutiveDashboardExcelReport,
    DashboardSummaryExcelReport,

    InstitutionCSVReport,
    SchoolCSVReport,
    DepartmentCSVReport,
    FacultyCSVReport,
    StudentCSVReport,

    ExecutiveDashboardCSVReport,
    DashboardSummaryCSVReport,

)


# ============================================================
# Institution Reports
# ============================================================

@login_required
def institution_pdf(request):

    return InstitutionPDFReport().generate()


@login_required
def institution_excel(request):

    return InstitutionExcelReport().generate()


@login_required
def institution_csv(request):

    return InstitutionCSVReport().generate()


# ============================================================
# School Reports
# ============================================================

@login_required
def school_pdf(request):

    return SchoolPDFReport().generate()


@login_required
def school_excel(request):

    return SchoolExcelReport().generate()


@login_required
def school_csv(request):

    return SchoolCSVReport().generate()


# ============================================================
# Department Reports
# ============================================================

@login_required
def department_pdf(request):

    return DepartmentPDFReport().generate()


@login_required
def department_excel(request):

    return DepartmentExcelReport().generate()


@login_required
def department_csv(request):

    return DepartmentCSVReport().generate()


# ============================================================
# Faculty Reports
# ============================================================

@login_required
def faculty_pdf(request):

    return FacultyPDFReport().generate()


@login_required
def faculty_excel(request):

    return FacultyExcelReport().generate()


@login_required
def faculty_csv(request):

    return FacultyCSVReport().generate()


# ============================================================
# CONTINUED IN PART-2
# ============================================================
# ============================================================
# report_views.py
# Institutional Brain
# Part-2
# ============================================================

# ============================================================
# Student Reports
# ============================================================

@login_required
def student_pdf(request):

    return StudentPDFReport().generate()


@login_required
def student_excel(request):

    return StudentExcelReport().generate()


@login_required
def student_csv(request):

    return StudentCSVReport().generate()


# ============================================================
# Institution Health Reports
# ============================================================

@login_required
def institution_health_pdf(request):

    return InstitutionHealthPDFReport().generate()


@login_required
def institution_health_excel(request):

    return InstitutionHealthExcelReport().generate()


# ============================================================
# School Health Reports
# ============================================================

@login_required
def school_health_pdf(request):

    return SchoolHealthPDFReport().generate()


@login_required
def school_health_excel(request):

    return SchoolHealthExcelReport().generate()


# ============================================================
# Department Health Reports
# ============================================================

@login_required
def department_health_pdf(request):

    return DepartmentHealthPDFReport().generate()


@login_required
def department_health_excel(request):

    return DepartmentHealthExcelReport().generate()


# ============================================================
# Department Risk Reports
# ============================================================

@login_required
def department_risk_pdf(request):

    return DepartmentRiskPDFReport().generate()


@login_required
def department_risk_excel(request):

    return DepartmentRiskExcelReport().generate()


# ============================================================
# Executive Dashboard Reports
# ============================================================

@login_required
def executive_dashboard_pdf(request):

    return ExecutiveDashboardPDFReport().generate()


@login_required
def executive_dashboard_excel(request):

    return ExecutiveDashboardExcelReport().generate()


@login_required
def executive_dashboard_csv(request):

    return ExecutiveDashboardCSVReport().generate()


# ============================================================
# Dashboard Summary Reports
# ============================================================

@login_required
def dashboard_summary_pdf(request):

    return DashboardSummaryPDFReport().generate()


@login_required
def dashboard_summary_excel(request):

    return DashboardSummaryExcelReport().generate()


@login_required
def dashboard_summary_csv(request):

    return DashboardSummaryCSVReport().generate()


# ============================================================
# CONTINUED IN PART-3
# ============================================================
# ============================================================
# Report Information
# ============================================================

@login_required
def report_information(request):

    return {

        "module": "Institutional Brain Reports",

        "version": "2.0",

        "available_reports": [

            "Institution PDF",

            "Institution Excel",

            "Institution CSV",

            "School PDF",

            "School Excel",

            "School CSV",

            "Department PDF",

            "Department Excel",

            "Department CSV",

            "Faculty PDF",

            "Faculty Excel",

            "Faculty CSV",

            "Student PDF",

            "Student Excel",

            "Student CSV",

            "Institution Health PDF",

            "Institution Health Excel",

            "School Health PDF",

            "School Health Excel",

            "Department Health PDF",

            "Department Health Excel",

            "Department Risk PDF",

            "Department Risk Excel",

            "Executive Dashboard PDF",

            "Executive Dashboard Excel",

            "Executive Dashboard CSV",

            "Dashboard Summary PDF",

            "Dashboard Summary Excel",

            "Dashboard Summary CSV",

        ],

    }


# ============================================================
# Health Check
# ============================================================

@login_required
def reports_health_check(request):

    from django.http import JsonResponse

    return JsonResponse(

        {

            "status": "OK",

            "module": "Reports",

            "version": "2.0",

        }

    )


# ============================================================
# Report Count
# ============================================================

@login_required
def report_count(request):

    from django.http import JsonResponse

    reports = [

        "Institution",

        "School",

        "Department",

        "Faculty",

        "Student",

        "Institution Health",

        "School Health",

        "Department Health",

        "Department Risk",

        "Executive Dashboard",

        "Dashboard Summary",

    ]

    return JsonResponse(

        {

            "total_reports": len(reports),

            "reports": reports,

        }

    )


# ============================================================
# END OF report_views.py
# ============================================================