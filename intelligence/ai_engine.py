from intelligence.models import (
    DepartmentHealth,
    DepartmentRisk,
)

from dashboard.models import (
    Department,
)


class AIEngine:

    # =====================================================
    # Executive AI Summary
    # =====================================================

    def executive_summary(self, profile=None):

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

        recommendations = []

        for department in departments:

            Strength = DepartmentHealth.objects.filter(
                department=department
            ).first()

            risk = DepartmentRisk.objects.filter(
                department=department
            ).first()

            if not Strength:
                continue

            message = []

            if Strength.health_score < 50:
                message.append(
                    "Overall department Strength is weak."
                )

            elif Strength.health_score < 75:
                message.append(
                    "Department performance is moderate."
                )

            else:
                message.append(
                    "Department is performing well."
                )

            if Strength.naac_score < 60:
                message.append(
                    "Improve NAAC documentation and evidence."
                )

            if Strength.nba_score != 0 and Strength.nba_score < 60:
                message.append(
                    "Improve CO-PO attainment and NBA outcomes."
                )

            if risk:

                if risk.risk_level == "HIGH":
                    message.append(
                        "Immediate intervention required."
                    )

                elif risk.risk_level == "MEDIUM":
                    message.append(
                        "Continuous monitoring recommended."
                    )

            recommendations.append({

                "department": department,

                "health_score": Strength.health_score,

                "risk_level": risk.risk_level if risk else "LOW",

                "recommendation": " ".join(message),

            })

        return recommendations

    # =====================================================
    # Department Recommendation
    # =====================================================

    def department_recommendation(self, department):

        Strength = DepartmentHealth.objects.filter(
            department=department
        ).first()

        risk = DepartmentRisk.objects.filter(
            department=department
        ).first()

        recommendations = []

        if not Strength:

            recommendations.append(
                "Department Strength data unavailable."
            )

            return recommendations

        if Strength.naac_score < 60:

            recommendations.append(
                "Improve NAAC metric performance."
            )

        if Strength.nba_score != 0:

            if Strength.nba_score < 60:

                recommendations.append(
                    "Improve NBA attainment."
                )

        if Strength.health_score < 50:

            recommendations.append(
                "Department requires strategic improvement plan."
            )

        elif Strength.health_score < 75:

            recommendations.append(
                "Department requires continuous improvement."
            )

        else:

            recommendations.append(
                "Maintain current performance."
            )

        if risk:

            if risk.risk_level == "HIGH":

                recommendations.append(
                    "High Risk: Immediate action required."
                )

            elif risk.risk_level == "MEDIUM":

                recommendations.append(
                    "Medium Risk: Monthly review recommended."
                )

        return recommendations

    # =====================================================
    # Weak Departments
    # =====================================================

    def weak_departments(self):

        weak = DepartmentHealth.objects.filter(
            health_score__lt=50
        ).select_related(
            "department"
        )

        return weak

    # =====================================================
    # Best Departments
    # =====================================================

    def best_departments(self):

        return DepartmentHealth.objects.order_by(
            "-health_score"
        )[:5]

    # =====================================================
    # Improvement Plan
    # =====================================================

    def improvement_plan(self, department):

        return {

            "department": department,

            "recommendations":
                self.department_recommendation(
                    department
                ),

            "timeline": "6 Months",

            "review_cycle": "Monthly",

            "owner": "HOD",

        }
        # =====================================================
    # System Dashboard
    # =====================================================

    def system_dashboard(self):

        return {
            "summary": self.executive_summary(),
            "weak_departments": list(self.weak_departments()),
            "best_departments": list(self.best_departments()),
        }

    # =====================================================
    # Institution Dashboard
    # =====================================================

    def institution_dashboard(self, institution):

        return self.system_dashboard()

    # =====================================================
    # School Dashboard
    # =====================================================

    def school_dashboard(self, school):

        recommendations = [
            item
            for item in self.executive_summary()
            if item["department"].school == school
        ]

        return {
            "summary": recommendations,
        }

    # =====================================================
    # Department Dashboard
    # =====================================================

    def department_dashboard(self, department):

        return self.improvement_plan(department)