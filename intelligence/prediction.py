from .models import DepartmentHealth
from .naac_analysis import calculate_naac_readiness


# =====================================
# ACCREDITATION RISK PREDICTION
# =====================================

def accreditation_risk():

    naac_score = calculate_naac_readiness()

    departments = DepartmentHealth.objects.all()

    weak_departments = []

    for d in departments:

        if d.health_score < 50:

            weak_departments.append(
                d.department.name
            )

    if naac_score >= 75:

        risk_level = "LOW"

    elif naac_score >= 50:

        risk_level = "MODERATE"

    else:

        risk_level = "HIGH"

    return {

        "naac_score": naac_score,
        "risk_level": risk_level,
        "weak_departments": weak_departments

    }