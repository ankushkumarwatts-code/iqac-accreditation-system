from naac.models import NAACMetricEntry


# =====================================
# NAAC READINESS CALCULATION
# =====================================

def calculate_naac_readiness():

    entries = NAACMetricEntry.objects.all()

    if not entries.exists():
        return 0

    achieved = sum(e.achieved_score for e in entries)
    target = sum(e.target_score for e in entries)

    if target == 0:
        return 0

    readiness = (achieved / target) * 100

    return round(readiness, 2)


# =====================================
# WEAK METRICS DETECTION
# =====================================

def weak_naac_metrics():

    entries = NAACMetricEntry.objects.all()

    weak = []

    for e in entries:

        if e.target_score == 0:
            continue

        score = (e.achieved_score / e.target_score) * 100

        if score < 50:

            weak.append({

                "metric": str(e.metric),
                "department": e.department.name if e.department else "Institution",
                "score": round(score, 2)

            })

    return weak