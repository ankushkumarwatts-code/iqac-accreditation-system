# ============================================================
# charts.py
# Institutional Brain Intelligence Engine
# Part-1
# ============================================================

from django.db.models import Count
from django.db.models import Avg

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

from .analytics import AnalyticsEngine
from .ranking_engine import RankingEngine
from .kpi_engine import KPIEngine
from .benchmark_engine import BenchmarkEngine
from .risk_engine import RiskEngine
from .scoring_engine import ScoringEngine


analytics = AnalyticsEngine()
ranking = RankingEngine()
kpi = KPIEngine()
benchmark = BenchmarkEngine()
risk = RiskEngine()
score = ScoringEngine()


# ============================================================
# Dashboard Chart Engine
# ============================================================

class DashboardChartEngine:

    def __init__(self):

        pass


# ============================================================
# Institution Health Chart
# ============================================================

    def institution_health_chart(self):

        labels = []

        values = []

        for obj in InstitutionHealth.objects.select_related(
            "institution"
        ):

            labels.append(

                obj.institution.name

            )

            values.append(

                obj.health_score

            )

        return {

            "title": "Institution Health",

            "type": "bar",

            "labels": labels,

            "datasets": [

                {

                    "label": "Health Score",

                    "data": values,

                }

            ],

        }


# ============================================================
# School Health Chart
# ============================================================

    def school_health_chart(self):

        labels = []

        values = []

        for obj in SchoolHealth.objects.select_related(
            "school"
        ):

            labels.append(

                obj.school.name

            )

            values.append(

                obj.health_score

            )

        return {

            "title": "School Health",

            "type": "bar",

            "labels": labels,

            "datasets": [

                {

                    "label": "Health Score",

                    "data": values,

                }

            ],

        }


# ============================================================
# Department Health Chart
# ============================================================

    def department_health_chart(self):

        labels = []

        values = []

        for obj in DepartmentHealth.objects.select_related(
            "department"
        ):

            labels.append(

                obj.department.name

            )

            values.append(

                obj.health_score

            )

        return {

            "title": "Department Health",

            "type": "bar",

            "labels": labels,

            "datasets": [

                {

                    "label": "Health Score",

                    "data": values,

                }

            ],

        }


# ============================================================
# Department Risk Chart
# ============================================================

    def department_risk_chart(self):

        labels = []

        values = []

        for obj in DepartmentRisk.objects.select_related(
            "department"
        ):

            labels.append(

                obj.department.name

            )

            values.append(

                obj.risk_score

            )

        return {

            "title": "Department Risk",

            "type": "bar",

            "labels": labels,

            "datasets": [

                {

                    "label": "Risk Score",

                    "data": values,

                }

            ],

        }


# ============================================================
# CONTINUED IN PART-2
# ============================================================
# ============================================================
# Faculty Performance Chart
# ============================================================

    def faculty_performance_chart(self):

        labels = []

        values = []

        for obj in Faculty.objects.all():

            labels.append(

                obj.name

            )

            values.append(

                getattr(

                    obj,

                    "performance_score",

                    0

                )

            )

        return {

            "title": "Faculty Performance",

            "type": "bar",

            "labels": labels,

            "datasets": [

                {

                    "label": "Performance",

                    "data": values,

                }

            ],

        }


# ============================================================
# Student Distribution Chart
# ============================================================

    def student_distribution_chart(self):

        data = (

            Student.objects

            .values("department__name")

            .annotate(

                total=Count("id")

            )

            .order_by(

                "department__name"

            )

        )

        return {

            "title": "Student Distribution",

            "type": "pie",

            "labels": [

                row["department__name"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Students",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# Department Faculty Count Chart
# ============================================================

    def department_faculty_chart(self):

        data = (

            Faculty.objects

            .values("department__name")

            .annotate(

                total=Count("id")

            )

            .order_by(

                "department__name"

            )

        )

        return {

            "title": "Faculty Distribution",

            "type": "doughnut",

            "labels": [

                row["department__name"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Faculty",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# School Department Count Chart
# ============================================================

    def school_department_chart(self):

        data = (

            Department.objects

            .values("school__name")

            .annotate(

                total=Count("id")

            )

            .order_by(

                "school__name"

            )

        )

        return {

            "title": "Departments by School",

            "type": "bar",

            "labels": [

                row["school__name"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Departments",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# Institution School Count Chart
# ============================================================

    def institution_school_chart(self):

        data = (

            School.objects

            .values("institution__name")

            .annotate(

                total=Count("id")

            )

            .order_by(

                "institution__name"

            )

        )

        return {

            "title": "Schools by Institution",

            "type": "bar",

            "labels": [

                row["institution__name"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Schools",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# CONTINUED IN PART-3
# ============================================================
# ============================================================
# KPI Achievement Chart
# ============================================================

    def kpi_achievement_chart(self):

        summary = kpi.dashboard_summary()

        return {

            "title": "KPI Achievement",

            "type": "doughnut",

            "labels": list(

                summary.keys()

            ),

            "datasets": [

                {

                    "label": "Achievement",

                    "data": list(

                        summary.values()

                    ),

                }

            ],

        }


# ============================================================
# Ranking Chart
# ============================================================

    def ranking_chart(self):

        data = ranking.institution_rankings()

        labels = []

        values = []

        for row in data:

            labels.append(

                row.get(

                    "name",

                    "Unknown"

                )

            )

            values.append(

                row.get(

                    "score",

                    0

                )

            )

        return {

            "title": "Institution Ranking",

            "type": "bar",

            "labels": labels,

            "datasets": [

                {

                    "label": "Ranking Score",

                    "data": values,

                }

            ],

        }


# ============================================================
# Benchmark Chart
# ============================================================

    def benchmark_chart(self):

        data = benchmark.institution_benchmark()

        labels = []

        values = []

        for row in data:

            labels.append(

                row.get(

                    "name",

                    "Unknown"

                )

            )

            values.append(

                row.get(

                    "benchmark",

                    0

                )

            )

        return {

            "title": "Benchmark Performance",

            "type": "line",

            "labels": labels,

            "datasets": [

                {

                    "label": "Benchmark",

                    "data": values,

                }

            ],

        }


# ============================================================
# Risk Distribution Chart
# ============================================================

    def risk_distribution_chart(self):

        data = (

            DepartmentRisk.objects

            .values(

                "risk_level"

            )

            .annotate(

                total=Count("id")

            )

            .order_by(

                "risk_level"

            )

        )

        return {

            "title": "Risk Distribution",

            "type": "pie",

            "labels": [

                row["risk_level"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Departments",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# Average Health Chart
# ============================================================

    def average_health_chart(self):

        avg_health = DepartmentHealth.objects.aggregate(

            average=Avg(

                "health_score"

            )

        )

        return {

            "title": "Average Department Health",

            "type": "gauge",

            "value": avg_health.get(

                "average",

                0

            ),

            "minimum": 0,

            "maximum": 100,

        }


# ============================================================
# CONTINUED IN PART-4
# ============================================================
# ============================================================
# Overall Score Chart
# ============================================================

    def overall_score_chart(self):

        summary = score.dashboard_scores()

        return {

            "title": "Overall Score",

            "type": "radar",

            "labels": list(

                summary.keys()

            ),

            "datasets": [

                {

                    "label": "Score",

                    "data": list(

                        summary.values()

                    ),

                }

            ],

        }


# ============================================================
# Analytics Summary Chart
# ============================================================

    def analytics_summary_chart(self):

        summary = analytics.dashboard_summary()

        return {

            "title": "Analytics Summary",

            "type": "polarArea",

            "labels": list(

                summary.keys()

            ),

            "datasets": [

                {

                    "label": "Analytics",

                    "data": list(

                        summary.values()

                    ),

                }

            ],

        }


# ============================================================
# Department Comparison Chart
# ============================================================

    def department_comparison_chart(self):

        labels = []

        values = []

        for obj in DepartmentHealth.objects.select_related(

            "department"

        ).order_by(

            "-health_score"

        ):

            labels.append(

                obj.department.name

            )

            values.append(

                obj.health_score

            )

        return {

            "title": "Department Comparison",

            "type": "horizontalBar",

            "labels": labels,

            "datasets": [

                {

                    "label": "Health Score",

                    "data": values,

                }

            ],

        }


# ============================================================
# Institution Comparison Chart
# ============================================================

    def institution_comparison_chart(self):

        labels = []

        values = []

        for obj in InstitutionHealth.objects.select_related(

            "institution"

        ):

            labels.append(

                obj.institution.name

            )

            values.append(

                obj.health_score

            )

        return {

            "title": "Institution Comparison",

            "type": "line",

            "labels": labels,

            "datasets": [

                {

                    "label": "Institution Health",

                    "data": values,

                }

            ],

        }


# ============================================================
# School Comparison Chart
# ============================================================

    def school_comparison_chart(self):

        labels = []

        values = []

        for obj in SchoolHealth.objects.select_related(

            "school"

        ):

            labels.append(

                obj.school.name

            )

            values.append(

                obj.health_score

            )

        return {

            "title": "School Comparison",

            "type": "line",

            "labels": labels,

            "datasets": [

                {

                    "label": "School Health",

                    "data": values,

                }

            ],

        }


# ============================================================
# Executive Dashboard Chart
# ============================================================

    def executive_dashboard_chart(self):

        return {

            "health": self.average_health_chart(),

            "risk": self.risk_distribution_chart(),

            "kpi": self.kpi_achievement_chart(),

            "ranking": self.ranking_chart(),

            "benchmark": self.benchmark_chart(),

            "score": self.overall_score_chart(),

        }


# ============================================================
# CONTINUED IN PART-5
# ============================================================
# ============================================================
# Student Gender Distribution Chart
# ============================================================

    def student_gender_distribution_chart(self):

        data = (

            Student.objects

            .values("gender")

            .annotate(

                total=Count("id")

            )

            .order_by(

                "gender"

            )

        )

        return {

            "title": "Student Gender Distribution",

            "type": "pie",

            "labels": [

                row["gender"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Students",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# Student Year Distribution Chart
# ============================================================

    def student_year_distribution_chart(self):

        data = (

            Student.objects

            .values("year")

            .annotate(

                total=Count("id")

            )

            .order_by(

                "year"

            )

        )

        return {

            "title": "Student Year Distribution",

            "type": "bar",

            "labels": [

                row["year"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Students",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# Faculty Department Distribution Chart
# ============================================================

    def faculty_department_distribution_chart(self):

        data = (

            Faculty.objects

            .values("department__name")

            .annotate(

                total=Count("id")

            )

            .order_by(

                "department__name"

            )

        )

        return {

            "title": "Faculty Distribution",

            "type": "doughnut",

            "labels": [

                row["department__name"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Faculty",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# School Performance Chart
# ============================================================

    def school_performance_chart(self):

        labels = []

        values = []

        for obj in SchoolHealth.objects.select_related(

            "school"

        ).order_by(

            "-health_score"

        ):

            labels.append(

                obj.school.name

            )

            values.append(

                obj.health_score

            )

        return {

            "title": "School Performance",

            "type": "bar",

            "labels": labels,

            "datasets": [

                {

                    "label": "Performance",

                    "data": values,

                }

            ],

        }


# ============================================================
# Institution Performance Trend
# ============================================================

    def institution_performance_trend_chart(self):

        labels = []

        values = []

        for obj in InstitutionHealth.objects.select_related(

            "institution"

        ):

            labels.append(

                obj.institution.name

            )

            values.append(

                obj.health_score

            )

        return {

            "title": "Institution Performance Trend",

            "type": "line",

            "labels": labels,

            "datasets": [

                {

                    "label": "Performance",

                    "data": values,

                    "fill": False,

                }

            ],

        }


# ============================================================
# CONTINUED IN PART-6
# ============================================================
# ============================================================
# Department Performance Trend Chart
# ============================================================

    def department_performance_trend_chart(self):

        labels = []

        values = []

        for obj in DepartmentHealth.objects.select_related(

            "department"

        ).order_by(

            "-health_score"

        ):

            labels.append(

                obj.department.name

            )

            values.append(

                obj.health_score

            )

        return {

            "title": "Department Performance Trend",

            "type": "line",

            "labels": labels,

            "datasets": [

                {

                    "label": "Department Health",

                    "data": values,

                    "fill": False,

                }

            ],

        }


# ============================================================
# Faculty Performance Trend Chart
# ============================================================

    def faculty_performance_trend_chart(self):

        labels = []

        values = []

        for obj in Faculty.objects.all():

            labels.append(

                obj.name

            )

            values.append(

                getattr(

                    obj,

                    "performance_score",

                    0

                )

            )

        return {

            "title": "Faculty Performance Trend",

            "type": "line",

            "labels": labels,

            "datasets": [

                {

                    "label": "Performance",

                    "data": values,

                    "fill": False,

                }

            ],

        }


# ============================================================
# Faculty Designation Distribution Chart
# ============================================================

    def faculty_designation_chart(self):

        data = (

            Faculty.objects

            .values(

                "designation"

            )

            .annotate(

                total=Count("id")

            )

            .order_by(

                "designation"

            )

        )

        return {

            "title": "Faculty Designation Distribution",

            "type": "pie",

            "labels": [

                row["designation"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Faculty",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# Student Admission Trend Chart
# ============================================================

    def student_admission_trend_chart(self):

        data = (

            Student.objects

            .values(

                "admission_year"

            )

            .annotate(

                total=Count("id")

            )

            .order_by(

                "admission_year"

            )

        )

        return {

            "title": "Student Admission Trend",

            "type": "line",

            "labels": [

                row["admission_year"]

                for row in data

            ],

            "datasets": [

                {

                    "label": "Admissions",

                    "data": [

                        row["total"]

                        for row in data

                    ],

                }

            ],

        }


# ============================================================
# Overall Statistics Chart
# ============================================================

    def overall_statistics_chart(self):

        return {

            "title": "Overall Statistics",

            "type": "bar",

            "labels": [

                "Institutions",

                "Schools",

                "Departments",

                "Faculty",

                "Students",

            ],

            "datasets": [

                {

                    "label": "Count",

                    "data": [

                        Institution.objects.count(),

                        School.objects.count(),

                        Department.objects.count(),

                        Faculty.objects.count(),

                        Student.objects.count(),

                    ],

                }

            ],

        }


# ============================================================
# CONTINUED IN PART-7
# ============================================================
# ============================================================
# Dashboard Summary Chart
# ============================================================

    def dashboard_summary_chart(self):

        summary = analytics.dashboard_summary()

        return {

            "title": "Dashboard Summary",

            "type": "bar",

            "labels": list(

                summary.keys()

            ),

            "datasets": [

                {

                    "label": "Summary",

                    "data": list(

                        summary.values()

                    ),

                }

            ],

        }


# ============================================================
# Executive Overview Chart
# ============================================================

    def executive_overview_chart(self):

        return {

            "title": "Executive Overview",

            "charts": [

                self.institution_health_chart(),

                self.school_health_chart(),

                self.department_health_chart(),

                self.department_risk_chart(),

                self.overall_statistics_chart(),

            ],

        }


# ============================================================
# Complete Dashboard Charts
# ============================================================

    def all_dashboard_charts(self):

        return {

            "institution_health":
                self.institution_health_chart(),

            "school_health":
                self.school_health_chart(),

            "department_health":
                self.department_health_chart(),

            "department_risk":
                self.department_risk_chart(),

            "faculty_performance":
                self.faculty_performance_chart(),

            "student_distribution":
                self.student_distribution_chart(),

            "faculty_distribution":
                self.faculty_department_distribution_chart(),

            "school_departments":
                self.school_department_chart(),

            "institution_schools":
                self.institution_school_chart(),

            "kpi":
                self.kpi_achievement_chart(),

            "ranking":
                self.ranking_chart(),

            "benchmark":
                self.benchmark_chart(),

            "risk":
                self.risk_distribution_chart(),

            "average_health":
                self.average_health_chart(),

            "overall_score":
                self.overall_score_chart(),

            "analytics":
                self.analytics_summary_chart(),

            "institution_comparison":
                self.institution_comparison_chart(),

            "school_comparison":
                self.school_comparison_chart(),

            "department_comparison":
                self.department_comparison_chart(),

            "gender_distribution":
                self.student_gender_distribution_chart(),

            "year_distribution":
                self.student_year_distribution_chart(),

            "school_performance":
                self.school_performance_chart(),

            "institution_trend":
                self.institution_performance_trend_chart(),

            "department_trend":
                self.department_performance_trend_chart(),

            "faculty_trend":
                self.faculty_performance_trend_chart(),

            "designation_distribution":
                self.faculty_designation_chart(),

            "admission_trend":
                self.student_admission_trend_chart(),

            "overall_statistics":
                self.overall_statistics_chart(),

            "dashboard_summary":
                self.dashboard_summary_chart(),

            "executive":
                self.executive_dashboard_chart(),

        }


# ============================================================
# Chart Information
# ============================================================

    def engine_information(self):

        return {

            "engine": "Dashboard Chart Engine",

            "version": "2.0",

            "charts_available": len(

                self.all_dashboard_charts()

            ),

            "framework": "Chart.js",

            "supported": [

                "Bar",

                "Line",

                "Pie",

                "Doughnut",

                "Radar",

                "PolarArea",

                "Gauge",

            ],

        }


# ============================================================
# END OF charts.py
# =========================================================###