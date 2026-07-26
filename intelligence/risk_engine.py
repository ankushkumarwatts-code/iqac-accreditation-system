from intelligence.models import (
    DepartmentRisk,
    DepartmentHealth,
)

from dashboard.models import (
    Department,
    School,
)


class RiskEngine:

    # ======================================================
    # Executive Risk Summary
    # ======================================================

    def summary(self, profile=None):

        departments = Department.objects.all()

        if profile:

            if profile.role in [
                "school_dean",
                "school_principal",
            ]:

                departments = departments.filter(
                    school=profile.school
                )

            elif profile.role == "hod":

                departments = departments.filter(
                    school=profile.department.school
                )

            elif profile.role == "faculty":

                departments = departments.filter(
                    id=profile.department.id
                )

        risks = DepartmentRisk.objects.filter(
            department__in=departments
        )

        return {

            "total_departments": departments.count(),

            "high": risks.filter(
                risk_level="HIGH"
            ).count(),

            "medium": risks.filter(
                risk_level="MEDIUM"
            ).count(),

            "low": risks.filter(
                risk_level="LOW"
            ).count(),

        }

    # ======================================================
    # Department Risk
    # ======================================================

    def department_risk(self, department):

        risk = DepartmentRisk.objects.filter(
            department=department
        ).first()

        health = DepartmentHealth.objects.filter(
            department=department
        ).first()

        if not risk:

            return {

                "department": department,

                "risk_level": "LOW",

                "naac_risk": "LOW",

                "nba_risk": "LOW",

                "issue": "",

                "health_score": (
                    health.health_score
                    if health else 0
                ),

            }

        return {

            "department": department,

            "risk_level": risk.risk_level,

            "naac_risk": risk.naac_risk,

            "nba_risk": risk.nba_risk,

            "issue": risk.issue,

            "health_score": (
                health.health_score
                if health else 0
            ),

        }

    # ======================================================
    # School Risk
    # ======================================================

    def school_risk(self, school):

        departments = Department.objects.filter(
            school=school
        )

        risks = DepartmentRisk.objects.filter(
            department__in=departments
        )

        return {

            "school": school,

            "high": risks.filter(
                risk_level="HIGH"
            ).count(),

            "medium": risks.filter(
                risk_level="MEDIUM"
            ).count(),

            "low": risks.filter(
                risk_level="LOW"
            ).count(),

        }

    # ======================================================
    # Critical Departments
    # ======================================================

    def critical_departments(self):

        risks = DepartmentRisk.objects.filter(
            risk_level="HIGH"
        ).select_related(
            "department"
        )

        data = []

        for risk in risks:

            data.append({

                "department": risk.department,

                "risk_level": risk.risk_level,

                "naac_risk": risk.naac_risk,

                "nba_risk": risk.nba_risk,

                "issue": risk.issue,

            })

        return data

    # ======================================================
    # Moderate Departments
    # ======================================================

    def moderate_departments(self):

        risks = DepartmentRisk.objects.filter(
            risk_level="MEDIUM"
        ).select_related(
            "department"
        )

        data = []

        for risk in risks:

            data.append({

                "department": risk.department,

                "risk_level": risk.risk_level,

                "naac_risk": risk.naac_risk,

                "nba_risk": risk.nba_risk,

                "issue": risk.issue,

            })

        return data

    # ======================================================
    # Low Risk Departments
    # ======================================================

    def low_risk_departments(self):

        risks = DepartmentRisk.objects.filter(
            risk_level="LOW"
        ).select_related(
            "department"
        )

        data = []

        for risk in risks:

            data.append({

                "department": risk.department,

                "risk_level": risk.risk_level,

                "naac_risk": risk.naac_risk,

                "nba_risk": risk.nba_risk,

                "issue": risk.issue,

            })

        return data

    # ======================================================
    # Dashboard Distribution
    # ======================================================

    def distribution(self):

        return {

            "high": DepartmentRisk.objects.filter(
                risk_level="HIGH"
            ).count(),

            "medium": DepartmentRisk.objects.filter(
                risk_level="MEDIUM"
            ).count(),

            "low": DepartmentRisk.objects.filter(
                risk_level="LOW"
            ).count(),

        }

    # ======================================================
    # Alerts
    # ======================================================

    def alerts(self):

        alerts = []

        for risk in DepartmentRisk.objects.filter(
            risk_level="HIGH"
        ):

            alerts.append(

                f"{risk.department.name} : {risk.issue}"

            )

        return alerts
        # ======================================================
    # System Dashboard
    # ======================================================

    def system_dashboard(self):

        return {
            "summary": self.summary(),
            "distribution": self.distribution(),
            "critical": self.critical_departments(),
            "moderate": self.moderate_departments(),
            "low": self.low_risk_departments(),
            "alerts": self.alerts(),
        }

    # ======================================================
    # Institution Dashboard
    # ======================================================

    def institution_dashboard(self, institution):

        return self.system_dashboard()

    # ======================================================
    # School Dashboard
    # ======================================================

    def school_dashboard(self, school):

        return {
            "summary": self.school_risk(school),
            "distribution": self.distribution(),
            "alerts": self.alerts(),
        }

    # ======================================================
    # Department Dashboard
    # ======================================================

    def department_dashboard(self, department):

        return self.department_risk(department)