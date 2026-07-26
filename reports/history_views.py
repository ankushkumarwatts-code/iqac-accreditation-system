from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import UploadLog


@login_required
def upload_history(request):

    uploads = UploadLog.objects.all().order_by(
        "-upload_date"
    )

    return render(
        request,
        "reports/upload_history.html",
        {
            "uploads": uploads
        }
    )