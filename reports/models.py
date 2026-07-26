from django.db import models
from django.contrib.auth.models import User

from dashboard.models import Institution, School, Department


# =====================================
# AI REPORT
# =====================================

class AIReport(models.Model):

    REPORT_TYPES = [
        ("NAAC", "NAAC"),
        ("NBA", "NBA"),
        ("NIRF", "NIRF"),
        ("DEPARTMENT", "Department"),
        ("SCHOOL", "School"),
        ("INSTITUTION", "Institution"),
    ]

    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("APPROVED", "Approved"),
        ("LOCKED", "Locked"),
    ]

    report_type = models.CharField(
        max_length=30,
        choices=REPORT_TYPES
    )

    title = models.CharField(max_length=500)

    event_name = models.CharField(
        max_length=500,
        blank=True
    )

    summary = models.TextField(blank=True)

    objectives = models.TextField(blank=True)

    outcomes = models.TextField(blank=True)

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        null=True,
        blank=True
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

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DRAFT"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_reports"
    )

    locked_at = models.DateTimeField(
        null=True,
        blank=True
    )

    is_pdf_generated = models.BooleanField(
        default=False
    )

    is_word_generated = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title


# =====================================
# UPLOAD LOG
# =====================================

class UploadLog(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    module = models.CharField(
        max_length=100
    )

    file_name = models.CharField(
        max_length=300
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    upload_date = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=50,
        default="SUCCESS"
    )

    error_message = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.module}"


# =====================================
# EVIDENCE REPOSITORY
# =====================================

class EvidenceRepository(models.Model):

    report = models.ForeignKey(
        AIReport,
        on_delete=models.CASCADE,
        related_name="evidences"
    )

    file = models.FileField(
        upload_to="evidence_repository/"
    )

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.file.name


# =====================================
# VALIDATION LOG
# =====================================

class ValidationLog(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    module = models.CharField(
        max_length=100
    )

    issue = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.module


# =====================================
# REPORT ACTIVITY LOG
# =====================================

class ReportActivity(models.Model):

    ACTIONS = [
        ("CREATED", "Created"),
        ("EDITED", "Edited"),
        ("APPROVED", "Approved"),
        ("LOCKED", "Locked"),
        ("PDF", "PDF Generated"),
        ("WORD", "Word Generated"),
    ]

    report = models.ForeignKey(
        AIReport,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=30,
        choices=ACTIONS
    )

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.report.title} - {self.action}"
    # =====================================
# ACTIVITY MANAGEMENT
# =====================================

class Activity(models.Model):

    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("SUBMITTED", "Submitted"),
        ("APPROVED", "Approved"),
        ("LOCKED", "Locked"),
    ]

    title = models.CharField(
        max_length=500
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    coordinator = models.CharField(
        max_length=255
    )

    venue = models.CharField(
        max_length=500,
        blank=True
    )

    activity_date = models.DateField(
        null=True,
        blank=True
    )

    participants = models.IntegerField(
        default=0
    )

    description = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DRAFT"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title