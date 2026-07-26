from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .benchmarking_engine import (
    calculate_naac_score,
    calculate_nba_score,
    calculate_health_index,
    calculate_risk_level,
)


@login_required
def benchmark_dashboard(request):

    context = {

        "naac_score": calculate_naac_score(),

        "nba_score": calculate_nba_score(),

        "health_index": calculate_health_index(),

        "risk_level": calculate_risk_level(),

    }

    return render(
        request,
        "reports/benchmark_dashboard.html",
        context
    )