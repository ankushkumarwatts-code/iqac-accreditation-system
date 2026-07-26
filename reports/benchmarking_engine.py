from naac.models import NAACMetricEntry
from nba.models import AttainmentEntry


# =====================================
# NAAC SCORE
# =====================================

def calculate_naac_score():

    entries = NAACMetricEntry.objects.all()

    total_percentage = 0
    total_entries = 0

    for entry in entries:

        try:

            if entry.target_score > 0:

                percentage = (
                    entry.achieved_score /
                    entry.target_score
                ) * 100

                total_percentage += percentage
                total_entries += 1

        except:
            pass

    if total_entries == 0:
        return 0

    return round(
        total_percentage / total_entries,
        2
    )


# =====================================
# NBA SCORE
# =====================================

def calculate_nba_score():

    attainments = AttainmentEntry.objects.all()

    total = 0
    count = 0

    for item in attainments:

        try:

            total += float(item.attainment)
            count += 1

        except:
            pass

    if count == 0:
        return 0

    return round(
        total / count,
        2
    )


# =====================================
# HEALTH INDEX
# =====================================

def calculate_health_index():

    naac = calculate_naac_score()
    nba = calculate_nba_score()

    return round(
        (naac + nba) / 2,
        2
    )


# =====================================
# RISK LEVEL
# =====================================

def calculate_risk_level():

    health = calculate_health_index()

    if health >= 80:
        return "LOW"

    elif health >= 60:
        return "MODERATE"

    else:
        return "HIGH"