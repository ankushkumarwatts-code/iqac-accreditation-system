from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .ai_report_engine import (
    generate_activity_report
)


@login_required
def ai_report_dashboard(request):

    report = None

    if request.method == "POST":

        activity_name = request.POST.get(
            "activity_name",
            ""
        )

        department = request.POST.get(
            "department",
            ""
        )

        coordinator = request.POST.get(
            "coordinator",
            ""
        )

        venue = request.POST.get(
            "venue",
            ""
        )

        date = request.POST.get(
            "date",
            ""
        )

        participants = request.POST.get(
            "participants",
            ""
        )

        description = request.POST.get(
            "description",
            ""
        )

        report = generate_activity_report(
            activity_name,
            department,
            coordinator,
            venue,
            date,
            participants,
            description
        )

    return render(
        request,
        "reports/ai_report_dashboard.html",
        {
            "report": report
        }
    )