# ============================================================
# reports.py
# Institutional Brain
# Part-1
# ============================================================

from io import BytesIO
import csv

from django.http import HttpResponse
from django.utils import timezone

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
)

from openpyxl import Workbook

from dashboard.models import (
    Institution,
    School,
    Department,
    Faculty,
    Student,
)

from intelligence.models import (
    InstitutionHealth,
    SchoolHealth,
    DepartmentHealth,
    DepartmentRisk,
)

from .services import DashboardService

service = DashboardService()


# ============================================================
# Report Builder
# ============================================================

class DashboardReportBuilder:

    def __init__(self):

        self.styles = getSampleStyleSheet()

    # ========================================================
    # Header
    # ========================================================

    def title(self, story, text):

        story.append(

            Paragraph(

                f"<b>{text}</b>",

                self.styles["Title"]

            )

        )

        story.append(

            Spacer(1, 0.25 * inch)

        )

    # ========================================================
    # Subtitle
    # ========================================================

    def subtitle(self, story, text):

        story.append(

            Paragraph(

                text,

                self.styles["Heading2"]

            )

        )

        story.append(

            Spacer(1, 0.15 * inch)

        )

    # ========================================================
    # Paragraph
    # ========================================================

    def paragraph(self, story, text):

        story.append(

            Paragraph(

                text,

                self.styles["BodyText"]

            )

        )

        story.append(

            Spacer(1, 0.10 * inch)

        )

    # ========================================================
    # Table
    # ========================================================

    def table(self, story, data):

        table = Table(data)

        table.setStyle(

            TableStyle([

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ])

        )

        story.append(table)

        story.append(

            Spacer(1, 0.25 * inch)

        )


# ============================================================
# PDF Export Base
# ============================================================

class PDFExporter:

    def __init__(self):

        self.builder = DashboardReportBuilder()

    def response(self, filename):

        response = HttpResponse(

            content_type="application/pdf"

        )

        response["Content-Disposition"] = (

            f'attachment; filename="{filename}"'

        )

        return response

    def document(self, response):

        return SimpleDocTemplate(

            response

        )


# ============================================================
# Excel Export Base
# ============================================================

class ExcelExporter:

    def workbook(self):

        return Workbook()

    def response(self, workbook, filename):

        response = HttpResponse(

            content_type=(
                "application/vnd.openxmlformats-"
                "officedocument.spreadsheetml.sheet"
            )

        )

        response["Content-Disposition"] = (

            f'attachment; filename="{filename}"'

        )

        workbook.save(response)

        return response


# ============================================================
# CSV Export Base
# ============================================================

class CSVExporter:

    def response(self, filename):

        response = HttpResponse(

            content_type="text/csv"

        )

        response["Content-Disposition"] = (

            f'attachment; filename="{filename}"'

        )

        return response

    def writer(self, response):

        return csv.writer(response)


# ============================================================
# CONTINUED IN PART-2
# ============================================================
# ============================================================
# reports.py
# Institutional Brain
# Part-1
# ============================================================

from io import BytesIO
import csv

from django.http import HttpResponse
from django.utils import timezone

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
)

from openpyxl import Workbook

from dashboard.models import (
    Institution,
    School,
    Department,
    Faculty,
    Student,
)

from intelligence.models import (
    InstitutionHealth,
    SchoolHealth,
    DepartmentHealth,
    DepartmentRisk,
)

from .services import DashboardService

service = DashboardService()


# ============================================================
# Report Builder
# ============================================================

class DashboardReportBuilder:

    def __init__(self):

        self.styles = getSampleStyleSheet()

    # ========================================================
    # Header
    # ========================================================

    def title(self, story, text):

        story.append(

            Paragraph(

                f"<b>{text}</b>",

                self.styles["Title"]

            )

        )

        story.append(

            Spacer(1, 0.25 * inch)

        )

    # ========================================================
    # Subtitle
    # ========================================================

    def subtitle(self, story, text):

        story.append(

            Paragraph(

                text,

                self.styles["Heading2"]

            )

        )

        story.append(

            Spacer(1, 0.15 * inch)

        )

    # ========================================================
    # Paragraph
    # ========================================================

    def paragraph(self, story, text):

        story.append(

            Paragraph(

                text,

                self.styles["BodyText"]

            )

        )

        story.append(

            Spacer(1, 0.10 * inch)

        )

    # ========================================================
    # Table
    # ========================================================

    def table(self, story, data):

        table = Table(data)

        table.setStyle(

            TableStyle([

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ])

        )

        story.append(table)

        story.append(

            Spacer(1, 0.25 * inch)

        )


# ============================================================
# PDF Export Base
# ============================================================

class PDFExporter:

    def __init__(self):

        self.builder = DashboardReportBuilder()

    def response(self, filename):

        response = HttpResponse(

            content_type="application/pdf"

        )

        response["Content-Disposition"] = (

            f'attachment; filename="{filename}"'

        )

        return response

    def document(self, response):

        return SimpleDocTemplate(

            response

        )


# ============================================================
# Excel Export Base
# ============================================================

class ExcelExporter:

    def workbook(self):

        return Workbook()

    def response(self, workbook, filename):

        response = HttpResponse(

            content_type=(
                "application/vnd.openxmlformats-"
                "officedocument.spreadsheetml.sheet"
            )

        )

        response["Content-Disposition"] = (

            f'attachment; filename="{filename}"'

        )

        workbook.save(response)

        return response


# ============================================================
# CSV Export Base
# ============================================================

class CSVExporter:

    def response(self, filename):

        response = HttpResponse(

            content_type="text/csv"

        )

        response["Content-Disposition"] = (

            f'attachment; filename="{filename}"'

        )

        return response

    def writer(self, response):

        return csv.writer(response)


# ============================================================
# CONTINUED IN PART-2
# ============================================================
# ============================================================
# Institution PDF Report
# ============================================================

class InstitutionPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "institution_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "Institution Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        data = [

            [

                "ID",

                "Institution"

            ]

        ]

        for obj in Institution.objects.all():

            data.append(

                [

                    obj.id,

                    obj.name,

                ]

            )

        self.builder.table(

            story,

            data

        )

        document.build(

            story

        )

        return response


# ============================================================
# School PDF Report
# ============================================================

class SchoolPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "school_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "School Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        data = [

            [

                "ID",

                "School",

                "Institution",

            ]

        ]

        for obj in School.objects.select_related(

            "institution"

        ):

            data.append(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.institution,

                        "name",

                        "-",

                    ),

                ]

            )

        self.builder.table(

            story,

            data

        )

        document.build(

            story

        )

        return response


# ============================================================
# Department PDF Report
# ============================================================

class DepartmentPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "department_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "Department Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        data = [

            [

                "ID",

                "Department",

                "School",

            ]

        ]

        for obj in Department.objects.select_related(

            "school"

        ):

            data.append(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.school,

                        "name",

                        "-",

                    ),

                ]

            )

        self.builder.table(

            story,

            data

        )

        document.build(

            story

        )

        return response


# ============================================================
# Faculty PDF Report
# ============================================================

class FacultyPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "faculty_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "Faculty Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        data = [

            [

                "ID",

                "Faculty",

                "Department",

            ]

        ]

        for obj in Faculty.objects.select_related(

            "department"

        ):

            data.append(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                ]

            )

        self.builder.table(

            story,

            data

        )

        document.build(

            story

        )

        return response


# ============================================================
# CONTINUED IN PART-3
# ============================================================
# ============================================================
# Student PDF Report
# ============================================================

class StudentPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "student_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "Student Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        data = [

            [

                "ID",

                "Student",

                "Department",

            ]

        ]

        for obj in Student.objects.select_related(

            "department"

        ):

            data.append(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                ]

            )

        self.builder.table(

            story,

            data

        )

        document.build(

            story

        )

        return response


# ============================================================
# Institution Health PDF Report
# ============================================================

class InstitutionHealthPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "institution_health_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "Institution Health Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        data = [

            [

                "Institution",

                "Health Score",

            ]

        ]

        for obj in InstitutionHealth.objects.select_related(

            "institution"

        ):

            data.append(

                [

                    getattr(

                        obj.institution,

                        "name",

                        "-",

                    ),

                    getattr(

                        obj,

                        "health_score",

                        "-",

                    ),

                ]

            )

        self.builder.table(

            story,

            data

        )

        document.build(

            story

        )

        return response


# ============================================================
# School Health PDF Report
# ============================================================

class SchoolHealthPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "school_health_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "School Health Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        data = [

            [

                "School",

                "Health Score",

            ]

        ]

        for obj in SchoolHealth.objects.select_related(

            "school"

        ):

            data.append(

                [

                    getattr(

                        obj.school,

                        "name",

                        "-",

                    ),

                    getattr(

                        obj,

                        "health_score",

                        "-",

                    ),

                ]

            )

        self.builder.table(

            story,

            data

        )

        document.build(

            story

        )

        return response


# ============================================================
# Department Health PDF Report
# ============================================================

class DepartmentHealthPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "department_health_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "Department Health Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        data = [

            [

                "Department",

                "Health Score",

            ]

        ]

        for obj in DepartmentHealth.objects.select_related(

            "department"

        ):

            data.append(

                [

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                    getattr(

                        obj,

                        "health_score",

                        "-",

                    ),

                ]

            )

        self.builder.table(

            story,

            data

        )

        document.build(

            story

        )

        return response


# ============================================================
# CONTINUED IN PART-4
# ============================================================
# ============================================================
# Department Risk PDF Report
# ============================================================

class DepartmentRiskPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "department_risk_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "Department Risk Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        data = [

            [

                "Department",

                "Risk Score",

                "Risk Level",

            ]

        ]

        for obj in DepartmentRisk.objects.select_related(

            "department"

        ):

            data.append(

                [

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                    getattr(

                        obj,

                        "risk_score",

                        "-",

                    ),

                    getattr(

                        obj,

                        "risk_level",

                        "-",

                    ),

                ]

            )

        self.builder.table(

            story,

            data

        )

        document.build(

            story

        )

        return response


# ============================================================
# Executive Dashboard PDF Report
# ============================================================

class ExecutiveDashboardPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "executive_dashboard_report.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "Executive Dashboard Report"

        )

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        dashboard = service.executive_dashboard()

        for key, value in dashboard.items():

            self.builder.subtitle(

                story,

                str(key).replace(

                    "_",

                    " "

                ).title()

            )

            self.builder.paragraph(

                story,

                str(value)

            )

        document.build(

            story

        )

        return response


# ============================================================
# Dashboard Summary PDF Report
# ============================================================

class DashboardSummaryPDFReport(PDFExporter):

    def generate(self):

        response = self.response(

            "dashboard_summary.pdf"

        )

        document = self.document(

            response

        )

        story = []

        self.builder.title(

            story,

            "Institutional Brain Dashboard Summary"

        )

        summary = service.dashboard_statistics()

        self.builder.paragraph(

            story,

            f"Generated : {timezone.now()}"

        )

        table_data = [

            [

                "Metric",

                "Value",

            ]

        ]

        for key, value in summary.items():

            table_data.append(

                [

                    str(

                        key

                    ).replace(

                        "_",

                        " "

                    ).title(),

                    str(value),

                ]

            )

        self.builder.table(

            story,

            table_data

        )

        document.build(

            story

        )

        return response


# ============================================================
# Institution Excel Report
# ============================================================

class InstitutionExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Institutions"

        sheet.append(

            [

                "ID",

                "Institution",

            ]

        )

        for obj in Institution.objects.all():

            sheet.append(

                [

                    obj.id,

                    obj.name,

                ]

            )

        return self.response(

            workbook,

            "institution_report.xlsx"

        )


# ============================================================
# School Excel Report
# ============================================================

class SchoolExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Schools"

        sheet.append(

            [

                "ID",

                "School",

                "Institution",

            ]

        )

        for obj in School.objects.select_related(

            "institution"

        ):

            sheet.append(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.institution,

                        "name",

                        "-",

                    ),

                ]

            )

        return self.response(

            workbook,

            "school_report.xlsx"

        )


# ============================================================
# CONTINUED IN PART-5
# ============================================================
# ============================================================
# Department Excel Report
# ============================================================

class DepartmentExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Departments"

        sheet.append(

            [

                "ID",

                "Department",

                "School",

            ]

        )

        for obj in Department.objects.select_related(

            "school"

        ):

            sheet.append(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.school,

                        "name",

                        "-",

                    ),

                ]

            )

        return self.response(

            workbook,

            "department_report.xlsx"

        )


# ============================================================
# Faculty Excel Report
# ============================================================

class FacultyExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Faculty"

        sheet.append(

            [

                "ID",

                "Faculty",

                "Department",

            ]

        )

        for obj in Faculty.objects.select_related(

            "department"

        ):

            sheet.append(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                ]

            )

        return self.response(

            workbook,

            "faculty_report.xlsx"

        )


# ============================================================
# Student Excel Report
# ============================================================

class StudentExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Students"

        sheet.append(

            [

                "ID",

                "Student",

                "Department",

            ]

        )

        for obj in Student.objects.select_related(

            "department"

        ):

            sheet.append(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                ]

            )

        return self.response(

            workbook,

            "student_report.xlsx"

        )


# ============================================================
# Institution Health Excel Report
# ============================================================

class InstitutionHealthExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Institution Health"

        sheet.append(

            [

                "Institution",

                "Health Score",

            ]

        )

        for obj in InstitutionHealth.objects.select_related(

            "institution"

        ):

            sheet.append(

                [

                    getattr(

                        obj.institution,

                        "name",

                        "-",

                    ),

                    getattr(

                        obj,

                        "health_score",

                        "-",

                    ),

                ]

            )

        return self.response(

            workbook,

            "institution_health.xlsx"

        )


# ============================================================
# School Health Excel Report
# ============================================================

class SchoolHealthExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "School Health"

        sheet.append(

            [

                "School",

                "Health Score",

            ]

        )

        for obj in SchoolHealth.objects.select_related(

            "school"

        ):

            sheet.append(

                [

                    getattr(

                        obj.school,

                        "name",

                        "-",

                    ),

                    getattr(

                        obj,

                        "health_score",

                        "-",

                    ),

                ]

            )

        return self.response(

            workbook,

            "school_health.xlsx"

        )


# ============================================================
# CONTINUED IN PART-6
# ============================================================
# ============================================================
# Department Health Excel Report
# ============================================================

class DepartmentHealthExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Department Health"

        sheet.append(

            [

                "Department",

                "Health Score",

            ]

        )

        for obj in DepartmentHealth.objects.select_related(

            "department"

        ):

            sheet.append(

                [

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                    getattr(

                        obj,

                        "health_score",

                        "-",

                    ),

                ]

            )

        return self.response(

            workbook,

            "department_health.xlsx"

        )


# ============================================================
# Department Risk Excel Report
# ============================================================

class DepartmentRiskExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Department Risk"

        sheet.append(

            [

                "Department",

                "Risk Score",

                "Risk Level",

            ]

        )

        for obj in DepartmentRisk.objects.select_related(

            "department"

        ):

            sheet.append(

                [

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                    getattr(

                        obj,

                        "risk_score",

                        "-",

                    ),

                    getattr(

                        obj,

                        "risk_level",

                        "-",

                    ),

                ]

            )

        return self.response(

            workbook,

            "department_risk.xlsx"

        )


# ============================================================
# Executive Dashboard Excel Report
# ============================================================

class ExecutiveDashboardExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Executive Dashboard"

        sheet.append(

            [

                "Metric",

                "Value",

            ]

        )

        dashboard = service.executive_dashboard()

        for key, value in dashboard.items():

            sheet.append(

                [

                    str(

                        key

                    ).replace(

                        "_",

                        " "

                    ).title(),

                    str(value),

                ]

            )

        return self.response(

            workbook,

            "executive_dashboard.xlsx"

        )


# ============================================================
# Dashboard Summary Excel Report
# ============================================================

class DashboardSummaryExcelReport(ExcelExporter):

    def generate(self):

        workbook = self.workbook()

        sheet = workbook.active

        sheet.title = "Dashboard Summary"

        sheet.append(

            [

                "Metric",

                "Value",

            ]

        )

        summary = service.dashboard_statistics()

        for key, value in summary.items():

            sheet.append(

                [

                    str(

                        key

                    ).replace(

                        "_",

                        " "

                    ).title(),

                    str(value),

                ]

            )

        return self.response(

            workbook,

            "dashboard_summary.xlsx"

        )


# ============================================================
# Institution CSV Report
# ============================================================

class InstitutionCSVReport(CSVExporter):

    def generate(self):

        response = self.response(

            "institution_report.csv"

        )

        writer = self.writer(

            response

        )

        writer.writerow(

            [

                "ID",

                "Institution",

            ]

        )

        for obj in Institution.objects.all():

            writer.writerow(

                [

                    obj.id,

                    obj.name,

                ]

            )

        return response


# ============================================================
# CONTINUED IN PART-7
# ============================================================
# ============================================================
# School CSV Report
# ============================================================

class SchoolCSVReport(CSVExporter):

    def generate(self):

        response = self.response(

            "school_report.csv"

        )

        writer = self.writer(

            response

        )

        writer.writerow(

            [

                "ID",

                "School",

                "Institution",

            ]

        )

        for obj in School.objects.select_related(

            "institution"

        ):

            writer.writerow(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.institution,

                        "name",

                        "-",

                    ),

                ]

            )

        return response


# ============================================================
# Department CSV Report
# ============================================================

class DepartmentCSVReport(CSVExporter):

    def generate(self):

        response = self.response(

            "department_report.csv"

        )

        writer = self.writer(

            response

        )

        writer.writerow(

            [

                "ID",

                "Department",

                "School",

            ]

        )

        for obj in Department.objects.select_related(

            "school"

        ):

            writer.writerow(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.school,

                        "name",

                        "-",

                    ),

                ]

            )

        return response


# ============================================================
# Faculty CSV Report
# ============================================================

class FacultyCSVReport(CSVExporter):

    def generate(self):

        response = self.response(

            "faculty_report.csv"

        )

        writer = self.writer(

            response

        )

        writer.writerow(

            [

                "ID",

                "Faculty",

                "Department",

            ]

        )

        for obj in Faculty.objects.select_related(

            "department"

        ):

            writer.writerow(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                ]

            )

        return response


# ============================================================
# Student CSV Report
# ============================================================

class StudentCSVReport(CSVExporter):

    def generate(self):

        response = self.response(

            "student_report.csv"

        )

        writer = self.writer(

            response

        )

        writer.writerow(

            [

                "ID",

                "Student",

                "Department",

            ]

        )

        for obj in Student.objects.select_related(

            "department"

        ):

            writer.writerow(

                [

                    obj.id,

                    obj.name,

                    getattr(

                        obj.department,

                        "name",

                        "-",

                    ),

                ]

            )

        return response


# ============================================================
# Dashboard Summary CSV Report
# ============================================================

class DashboardSummaryCSVReport(CSVExporter):

    def generate(self):

        response = self.response(

            "dashboard_summary.csv"

        )

        writer = self.writer(

            response

        )

        writer.writerow(

            [

                "Metric",

                "Value",

            ]

        )

        summary = service.dashboard_statistics()

        for key, value in summary.items():

            writer.writerow(

                [

                    str(

                        key

                    ).replace(

                        "_",

                        " "

                    ).title(),

                    str(value),

                ]

            )

        return response


# ============================================================
# Executive Dashboard CSV Report
# ============================================================

class ExecutiveDashboardCSVReport(CSVExporter):

    def generate(self):

        response = self.response(

            "executive_dashboard.csv"

        )

        writer = self.writer(

            response

        )

        writer.writerow(

            [

                "Metric",

                "Value",

            ]

        )

        dashboard = service.executive_dashboard()

        for key, value in dashboard.items():

            writer.writerow(

                [

                    str(

                        key

                    ).replace(

                        "_",

                        " "

                    ).title(),

                    str(value),

                ]

            )

        return response


# ============================================================
# END OF reports.py
# ============================================================