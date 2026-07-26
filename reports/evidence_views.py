from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import EvidenceRepository


@login_required
def evidence_repository(request):

    evidences = EvidenceRepository.objects.all().order_by(
        "-uploaded_at"
    )

    return render(
        request,
        "reports/evidence_repository.html",
        {
            "evidences": evidences
        }
    )