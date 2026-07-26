from django.db import models
from django.contrib.auth.models import User


# =====================================
# INSTITUTION
# =====================================

class Institution(models.Model):

    name = models.CharField(max_length=200)

    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# =====================================
# SCHOOL
# =====================================

class School(models.Model):

    name = models.CharField(max_length=200)

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name="schools"
    )

    def __str__(self):
        return self.name


# =====================================
# DEPARTMENT
# =====================================

class Department(models.Model):

    name = models.CharField(max_length=200)

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="departments"
    )

    established_year = models.IntegerField(default=2000)

    def __str__(self):
        return f"{self.name} ({self.school.name})"


# =====================================
# USER PROFILE (🔥 MAIN CONTROL)
# =====================================

class UserProfile(models.Model):

    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("principal", "Principal"),
        ("hod", "HOD"),
        ("faculty", "Faculty"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES
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

    def __str__(self):
        return f"{self.user.username} ({self.role})"