from django.db import models
from dashboard.models import Department


# ==========================================
# PROGRAM
# ==========================================
class Program(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programs"
    )
    duration_years = models.IntegerField(default=4)

    def __str__(self):
        return self.name


# ==========================================
# COURSE
# ==========================================
class Course(models.Model):
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name="courses"
    )
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    credits = models.FloatField(default=3)

    class Meta:
        unique_together = ("program", "code")

    def __str__(self):
        return f"{self.code} - {self.name}"


# ==========================================
# COURSE OUTCOME (CO)
# ==========================================
class CourseOutcome(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_outcomes"
    )
    code = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        unique_together = ("course", "code")

    def __str__(self):
        return f"{self.course.code} - {self.code}"


# ==========================================
# CO ATTAINMENT ENTRY
# ==========================================
class AttainmentEntry(models.Model):
    course_outcome = models.ForeignKey(
        CourseOutcome,
        on_delete=models.CASCADE,
        related_name="attainments"
    )
    year = models.IntegerField()
    attainment_percentage = models.FloatField()

    class Meta:
        unique_together = ("course_outcome", "year")

    def __str__(self):
        return f"{self.course_outcome} - {self.year} - {self.attainment_percentage}%"