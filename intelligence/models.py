from django.db import models

from dashboard.models import Department, Faculty, School, Institution
from naac.models import NAACMetricEntry

from nba.models import AttainmentEntry, COPOMapping
from academics.models import CourseOutcome


# =====================================
# NBA SCORE CALCULATION
# =====================================

def calculate_nba_score(department):

    outcomes = CourseOutcome.objects.filter(
        course__program__department=department
    )

    attainment_values = []

    for co in outcomes:

        entries = AttainmentEntry.objects.filter(
            course_outcome=co
        )

        if entries.exists():

            avg_attainment = sum(
                e.attainment for e in entries
            ) / entries.count()

            mappings = COPOMapping.objects.filter(
                course_outcome=co
            )

            for m in mappings:
                weighted = avg_attainment * m.mapping_strength
                attainment_values.append(weighted)

    if attainment_values:
        return round(sum(attainment_values) / len(attainment_values), 2)

    return 0


# =====================================
# NAAC SCORE CALCULATION
# =====================================

def calculate_naac_score(department):

    entries = NAACMetricEntry.objects.filter(
        department=department
    )

    if entries.exists():

        achieved = sum(
            e.achieved_score for e in entries if e.achieved_score is not None
        )

        target = sum(
            e.target_score for e in entries if e.target_score is not None
        )

        return (achieved / target) * 100 if target > 0 else 0

    return 0


# =====================================
# DEPARTMENT HEALTH
# =====================================

class DepartmentHealth(models.Model):

    department = models.OneToOneField(
        Department,
        on_delete=models.CASCADE
    )

    naac_score = models.FloatField(default=0)
    nba_score = models.FloatField(default=0)

    health_score = models.FloatField(default=0)

    status = models.CharField(max_length=50, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def calculate_health(self):

        nba_score = calculate_nba_score(self.department)
        naac_score = calculate_naac_score(self.department)

        self.nba_score = nba_score
        self.naac_score = naac_score

        if nba_score == 0:
            self.health_score = naac_score
        else:
            self.health_score = (0.5 * naac_score + 0.5 * nba_score)

        if self.health_score >= 75:
            self.status = "Strong"
        elif self.health_score >= 50:
            self.status = "Moderate"
        else:
            self.status = "Weak"

        self.save()

    def __str__(self):
        return f"{self.department.name} Health"


# =====================================
# SCHOOL HEALTH
# =====================================

class SchoolHealth(models.Model):

    school = models.OneToOneField(
        School,
        on_delete=models.CASCADE
    )

    health_score = models.FloatField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    def calculate_health(self):

        departments = Department.objects.filter(
            school=self.school
        )

        scores = []

        for dept in departments:

            dh = DepartmentHealth.objects.filter(
                department=dept
            ).first()

            if dh:
                scores.append(dh.health_score)

        if scores:
            self.health_score = round(sum(scores) / len(scores), 2)
        else:
            self.health_score = 0

        self.save()

    def __str__(self):
        return f"{self.school.name} Health"


# =====================================
# INSTITUTION HEALTH
# =====================================

class InstitutionHealth(models.Model):

    institution = models.OneToOneField(
        Institution,
        on_delete=models.CASCADE
    )

    health_score = models.FloatField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    def calculate_health(self):

        schools = School.objects.filter(
            institution=self.institution
        )

        scores = []

        for school in schools:

            sh = SchoolHealth.objects.filter(
                school=school
            ).first()

            if sh:
                scores.append(sh.health_score)

        if scores:
            self.health_score = round(sum(scores) / len(scores), 2)
        else:
            self.health_score = 0

        self.save()

    def __str__(self):
        return f"{self.institution.name} Health"


# =====================================
# DEPARTMENT RISK (FINAL UPGRADE)
# =====================================

class DepartmentRisk(models.Model):

    department = models.OneToOneField(
        Department,
        on_delete=models.CASCADE
    )

    nba_score = models.FloatField(default=0)
    naac_score = models.FloatField(default=0)

    # 🔥 NEW FIELDS
    nba_risk = models.CharField(max_length=10, default="LOW")
    naac_risk = models.CharField(max_length=10, default="LOW")

    risk_level = models.CharField(max_length=10, default="LOW")

    issue = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def detect_risk(self):

        issues = []

        # 🔵 NAAC RISK
        if self.naac_score < 40:
            self.naac_risk = "HIGH"
            issues.append("Low NAAC")
        elif self.naac_score < 60:
            self.naac_risk = "MEDIUM"
        else:
            self.naac_risk = "LOW"

        # 🟠 NBA RISK
        if self.nba_score != 0:
            if self.nba_score < 40:
                self.nba_risk = "HIGH"
                issues.append("Low NBA")
            elif self.nba_score < 60:
                self.nba_risk = "MEDIUM"
            else:
                self.nba_risk = "LOW"
        else:
            self.nba_risk = "N/A"

        # 🔥 OVERALL
        if self.naac_risk == "HIGH" or self.nba_risk == "HIGH":
            self.risk_level = "HIGH"
        elif self.naac_risk == "MEDIUM" or self.nba_risk == "MEDIUM":
            self.risk_level = "MEDIUM"
        else:
            self.risk_level = "LOW"

        self.issue = ", ".join(issues)

        self.save()

    def __str__(self):
        return f"{self.department.name} Risk"