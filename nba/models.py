from django.db import models


# ==========================================
# PROGRAM OUTCOME (PO)
# ==========================================
class ProgramOutcome(models.Model):
    """
    Represents Program Outcomes (PO1, PO2, etc.)
    Each PO belongs to a Program
    """

    program = models.ForeignKey(
        'academics.Program',
        on_delete=models.CASCADE,
        related_name="program_outcomes"
    )

    code = models.CharField(max_length=10)  # Example: PO1, PO2
    description = models.TextField()

    class Meta:
        unique_together = ("program", "code")
        ordering = ["program", "code"]

    def __str__(self):
        return f"{self.program.name} - {self.code}"


# ==========================================
# CO - PO MAPPING
# ==========================================
class COPOMapping(models.Model):
    """
    Mapping between Course Outcome (CO) and Program Outcome (PO)
    with mapping strength (0–3 scale)
    """

    course_outcome = models.ForeignKey(
        'academics.CourseOutcome',
        on_delete=models.CASCADE,
        related_name="po_mappings"
    )

    program_outcome = models.ForeignKey(
        ProgramOutcome,
        on_delete=models.CASCADE,
        related_name="co_mappings"
    )

    mapping_strength = models.IntegerField(default=1)  # Scale: 0–3

    class Meta:
        unique_together = ("course_outcome", "program_outcome")
        ordering = ["program_outcome"]

    def __str__(self):
        return f"{self.course_outcome.code} → {self.program_outcome.code}"


# ==========================================
# CO ATTAINMENT ENTRY
# ==========================================
class AttainmentEntry(models.Model):
    """
    Stores attainment values of each Course Outcome (CO)
    This is the MAIN DATA used for NBA analytics
    """

    course_outcome = models.ForeignKey(
        'academics.CourseOutcome',
        on_delete=models.CASCADE,
        related_name="attainment_entries"
    )

    attainment = models.FloatField()  # Example: 2.5, 3.0

    year = models.IntegerField()

    class Meta:
        ordering = ["course_outcome"]

    def __str__(self):
        return f"{self.course_outcome.code} - {self.attainment}"


# ==========================================
# 🔥 OPTIONAL (ADVANCED - AUTO PO ATTAINMENT)
# ==========================================
class POAttainment(models.Model):
    """
    Stores calculated PO attainment (optional cache table)
    Useful for faster dashboard rendering
    """

    program_outcome = models.ForeignKey(
        ProgramOutcome,
        on_delete=models.CASCADE,
        related_name="attainments"
    )

    score = models.FloatField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.program_outcome.code} - {self.score}"


    score = models.FloatField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.program_outcome.code} - {self.score}"


class NBACriteria(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class NBAMetric(models.Model):
    criteria = models.ForeignKey(NBACriteria, on_delete=models.CASCADE, related_name="metrics")
    title = models.CharField(max_length=255)
    template = models.FileField(upload_to='nba/templates/', null=True, blank=True)
    filled_file = models.FileField(upload_to='nba/uploads/', null=True, blank=True)
    template_name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.title