from django.db import models
from django.conf import settings
from dashboard.models import School, Department


# ==========================
# NAAC CRITERIA
# ==========================
class NAACCriteria(models.Model):

    code = models.CharField(max_length=5, unique=True)  # C1, C2
    name = models.CharField(max_length=255)
    weightage = models.FloatField(default=0)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"


# ==========================
# NAAC METRICS
# ==========================
class NAACMetric(models.Model):

    criteria = models.ForeignKey(
        NAACCriteria,
        on_delete=models.CASCADE,
        related_name="metrics"
    )

    metric_code = models.CharField(max_length=10)
    description = models.TextField()
    max_score = models.FloatField(default=100)

    template_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ("criteria", "metric_code")
        ordering = ["metric_code"]

    def __str__(self):
        return f"{self.metric_code} ({self.criteria.code})"

# ==========================
# NAAC METRIC ENTRY
# ==========================
class NAACMetricEntry(models.Model):

    metric = models.ForeignKey(
        NAACMetric,
        on_delete=models.CASCADE,
        related_name="entries"
    )

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    achieved_score = models.FloatField(default=0)
    target_score = models.FloatField(default=0)

    year = models.IntegerField()

    entered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-year"]
        indexes = [
            models.Index(fields=["year"]),
        ]

    def percentage(self):
        if not self.target_score or self.target_score == 0:
            return 0
        return round((self.achieved_score / self.target_score) * 100, 2)

    def __str__(self):
        dept = self.department.name if self.department else "N/A"
        return f"{self.metric.metric_code} - {dept} - {self.year}"
class NAACExcelUpload(models.Model):
    file = models.FileField(upload_to='naac/excel/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"NAAC Excel - {self.uploaded_at}"