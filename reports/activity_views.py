from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Activity
from dashboard.models import Department


@login_required
def activity_dashboard(request):

    if request.method == "POST":

        activity_name = request.POST.get("activity_name")
        department_id = request.POST.get("department")
        coordinator = request.POST.get("coordinator")
        venue = request.POST.get("venue")
        activity_date = request.POST.get("activity_date")
        description = request.POST.get("description")

        department = Department.objects.get(
            id=department_id
        )

        Activity.objects.create(
            title=activity_name,
            department=department,
            coordinator=coordinator,
            venue=venue,
            activity_date=activity_date,
            description=description,
            created_by=request.user
        )

        return redirect(
            "activity_dashboard"
        )

    departments = Department.objects.all()

    activities = Activity.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "reports/activity_dashboard.html",
        {
            "departments": departments,
            "activities": activities,
        }
    )