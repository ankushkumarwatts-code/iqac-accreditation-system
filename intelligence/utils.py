# ============================================================
# utils.py
# Institutional Brain Intelligence Engine
# Part-1
# ============================================================

import json
import math
from datetime import datetime
from datetime import date

from django.core.paginator import Paginator
from django.http import JsonResponse


# ============================================================
# Percentage Utilities
# ============================================================

class PercentageUtils:

    @staticmethod
    def calculate(obtained, total):

        if total in [0, None]:

            return 0

        return round(

            (obtained / total) * 100,

            2

        )

    @staticmethod
    def average(values):

        if not values:

            return 0

        return round(

            sum(values) / len(values),

            2

        )

    @staticmethod
    def progress(current, target):

        if target == 0:

            return 0

        return round(

            current * 100 / target,

            2

        )


# ============================================================
# Grade Utilities
# ============================================================

class GradeUtils:

    @staticmethod
    def grade(score):

        if score >= 90:

            return "A+"

        if score >= 80:

            return "A"

        if score >= 70:

            return "B+"

        if score >= 60:

            return "B"

        if score >= 50:

            return "C"

        if score >= 40:

            return "D"

        return "F"

    @staticmethod
    def remarks(score):

        if score >= 90:

            return "Excellent"

        if score >= 80:

            return "Very Good"

        if score >= 70:

            return "Good"

        if score >= 60:

            return "Average"

        if score >= 50:

            return "Below Average"

        return "Poor"


# ============================================================
# Health Utilities
# ============================================================

class HealthUtils:

    @staticmethod
    def status(score):

        if score >= 90:

            return "Excellent"

        if score >= 75:

            return "Healthy"

        if score >= 60:

            return "Moderate"

        if score >= 40:

            return "Weak"

        return "Critical"

    @staticmethod
    def color(score):

        if score >= 90:

            return "#28a745"

        if score >= 75:

            return "#17a2b8"

        if score >= 60:

            return "#ffc107"

        if score >= 40:

            return "#fd7e14"

        return "#dc3545"


# ============================================================
# Risk Utilities
# ============================================================

class RiskUtils:

    @staticmethod
    def level(score):

        if score >= 80:

            return "Critical"

        if score >= 60:

            return "High"

        if score >= 40:

            return "Moderate"

        if score >= 20:

            return "Low"

        return "Very Low"

    @staticmethod
    def color(score):

        if score >= 80:

            return "#dc3545"

        if score >= 60:

            return "#fd7e14"

        if score >= 40:

            return "#ffc107"

        if score >= 20:

            return "#17a2b8"

        return "#28a745"


# ============================================================
# CONTINUED IN PART-2
# ============================================================
# ============================================================
# Date Utilities
# ============================================================

class DateUtils:

    @staticmethod
    def today():

        return date.today()

    @staticmethod
    def now():

        return datetime.now()

    @staticmethod
    def format(value, fmt="%d-%m-%Y"):

        if not value:

            return ""

        return value.strftime(fmt)

    @staticmethod
    def datetime_format(value, fmt="%d-%m-%Y %H:%M:%S"):

        if not value:

            return ""

        return value.strftime(fmt)


# ============================================================
# Progress Utilities
# ============================================================

class ProgressUtils:

    @staticmethod
    def percentage(current, total):

        if total == 0:

            return 0

        return round(

            current * 100 / total,

            2

        )

    @staticmethod
    def completed(current, total):

        return current >= total

    @staticmethod
    def remaining(current, total):

        return max(

            total - current,

            0

        )


# ============================================================
# Score Utilities
# ============================================================

class ScoreUtils:

    @staticmethod
    def normalize(score, maximum=100):

        if score > maximum:

            score = maximum

        if score < 0:

            score = 0

        return score

    @staticmethod
    def average(scores):

        if not scores:

            return 0

        return round(

            sum(scores) / len(scores),

            2

        )

    @staticmethod
    def total(scores):

        return round(

            sum(scores),

            2

        )


# ============================================================
# Color Utilities
# ============================================================

class ColorUtils:

    COLORS = {

        "green": "#28a745",

        "blue": "#007bff",

        "yellow": "#ffc107",

        "orange": "#fd7e14",

        "red": "#dc3545",

        "purple": "#6f42c1",

        "grey": "#6c757d",

    }

    @staticmethod
    def get(name):

        return ColorUtils.COLORS.get(

            name,

            "#6c757d"

        )


# ============================================================
# Badge Utilities
# ============================================================

class BadgeUtils:

    @staticmethod
    def badge(status):

        mapping = {

            "Excellent": "success",

            "Healthy": "success",

            "Good": "primary",

            "Moderate": "warning",

            "Weak": "danger",

            "Critical": "danger",

        }

        return mapping.get(

            status,

            "secondary"

        )


# ============================================================
# CONTINUED IN PART-3
# ============================================================
# ============================================================
# Label Utilities
# ============================================================

class LabelUtils:

    @staticmethod
    def title(text):

        if not text:

            return ""

        return str(

            text

        ).replace(

            "_",

            " "

        ).title()

    @staticmethod
    def upper(text):

        return str(text).upper()

    @staticmethod
    def lower(text):

        return str(text).lower()


# ============================================================
# JSON Utilities
# ============================================================

class JSONUtils:

    @staticmethod
    def dumps(data):

        return json.dumps(

            data,

            default=str,

            indent=4

        )

    @staticmethod
    def response(data):

        return JsonResponse(

            data,

            safe=False

        )


# ============================================================
# Pagination Utilities
# ============================================================

class PaginationUtils:

    @staticmethod
    def paginate(queryset, page, size=20):

        paginator = Paginator(

            queryset,

            size

        )

        return paginator.get_page(

            page

        )


# ============================================================
# Search Utilities
# ============================================================

class SearchUtils:

    @staticmethod
    def contains(value, keyword):

        if value is None:

            return False

        return keyword.lower() in str(

            value

        ).lower()

    @staticmethod
    def starts_with(value, keyword):

        if value is None:

            return False

        return str(

            value

        ).lower().startswith(

            keyword.lower()

        )


# ============================================================
# Math Utilities
# ============================================================

class MathUtils:

    @staticmethod
    def percentage(value, total):

        if total == 0:

            return 0

        return round(

            (value / total) * 100,

            2

        )

    @staticmethod
    def round2(value):

        return round(

            value,

            2

        )

    @staticmethod
    def sqrt(value):

        return math.sqrt(

            value

        )

    @staticmethod
    def square(value):

        return value ** 2


# ============================================================
# CONTINUED IN PART-4
# ============================================================
# ============================================================
# Response Utilities
# ============================================================

class ResponseUtils:

    @staticmethod
    def success(message="Success", data=None):

        return {

            "status": True,

            "message": message,

            "data": data,

        }

    @staticmethod
    def error(message="Error", data=None):

        return {

            "status": False,

            "message": message,

            "data": data,

        }

    @staticmethod
    def info(message="Information", data=None):

        return {

            "status": "info",

            "message": message,

            "data": data,

        }


# ============================================================
# Export Utilities
# ============================================================

class ExportUtils:

    @staticmethod
    def filename(prefix, extension):

        timestamp = datetime.now().strftime(

            "%Y%m%d_%H%M%S"

        )

        return (

            f"{prefix}_{timestamp}.{extension}"

        )

    @staticmethod
    def report_name(title):

        return title.replace(

            " ",

            "_"

        ).lower()


# ============================================================
# Chart Utilities
# ============================================================

class ChartUtils:

    @staticmethod
    def dataset(label, values):

        return {

            "label": label,

            "data": values,

        }

    @staticmethod
    def chart(title, chart_type, labels, datasets):

        return {

            "title": title,

            "type": chart_type,

            "labels": labels,

            "datasets": datasets,

        }


# ============================================================
# Ranking Utilities
# ============================================================

class RankingUtils:

    @staticmethod
    def rank(items, key):

        return sorted(

            items,

            key=lambda x: x.get(

                key,

                0

            ),

            reverse=True,

        )

    @staticmethod
    def top(items, number=10):

        return items[:number]


# ============================================================
# Dashboard Utilities
# ============================================================

class DashboardUtils:

    @staticmethod
    def summary(title, value):

        return {

            "title": title,

            "value": value,

        }

    @staticmethod
    def card(title, value, color="primary"):

        return {

            "title": title,

            "value": value,

            "color": color,

        }

    @staticmethod
    def metric(name, score, status):

        return {

            "metric": name,

            "score": score,

            "status": status,

        }


# ============================================================
# Validation Utilities
# ============================================================

class ValidationUtils:

    @staticmethod
    def is_number(value):

        return isinstance(

            value,

            (int, float)

        )

    @staticmethod
    def is_empty(value):

        return value in [

            None,

            "",

            [],

            {},

        ]

    @staticmethod
    def positive(value):

        return value >= 0


# ============================================================
# Engine Information
# ============================================================

class EngineInformation:

    @staticmethod
    def information():

        return {

            "engine": "Institutional Brain Utility Engine",

            "version": "2.0",

            "module": "utils.py",

            "framework": "Django",

            "status": "Ready",

            "components": [

                "PercentageUtils",

                "GradeUtils",

                "HealthUtils",

                "RiskUtils",

                "DateUtils",

                "ProgressUtils",

                "ScoreUtils",

                "ColorUtils",

                "BadgeUtils",

                "LabelUtils",

                "JSONUtils",

                "PaginationUtils",

                "SearchUtils",

                "MathUtils",

                "ResponseUtils",

                "ExportUtils",

                "ChartUtils",

                "RankingUtils",

                "DashboardUtils",

                "ValidationUtils",

            ],

        }


# ============================================================
# END OF utils.py
# ============================================================
