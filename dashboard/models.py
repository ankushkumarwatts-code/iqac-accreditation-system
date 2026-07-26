from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class BaseModel(models.Model):
    """
    Common fields for all future models.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# ======================================================
# USER PROFILE (🔥 FIXED – MOST IMPORTANT)
# ======================================================

class UserProfile(models.Model):

    ROLE_CHOICES = [

        ("campus_md", "Campus MD"),
        ("campus_director", "Campus Director"),
        ("campus_deputy_director", "Campus Deputy Director"),

        ("iqac_dean", "IQAC Dean"),
        ("iqac_deputy_dean", "IQAC Deputy Dean"),
        ("iqac_cell_head", "IQAC Cell Head"),

        ("school_dean", "School Dean"),
        ("school_principal", "School Principal"),

        ("research_cell_head", "Research Cell Head"),

        ("hod", "Head of Department"),

        ("faculty", "Faculty"),

        ("admin", "System Administrator"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES
    )

    department = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    school = models.ForeignKey(
        'School',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )

    institution = models.ForeignKey(
        'Institution',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )
    def __str__(self):
        return f"{self.user.username} - {self.role}"


# ======================================================
# INSTITUTION
# ======================================================

class Institution(models.Model):

    name = models.CharField(max_length=300)
    established_year = models.IntegerField()

    naac_grade = models.CharField(max_length=10, blank=True, null=True)
    autonomous_status = models.BooleanField(default=False)

    affiliated_university = models.CharField(max_length=300, blank=True, null=True)

    vision = models.TextField()
    mission = models.TextField()

    def __str__(self):
        return self.name


# ======================================================
# SCHOOL
# ======================================================

class School(models.Model):

    name = models.CharField(max_length=200)

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name="schools"
    )

    dean_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


# ======================================================
# DEPARTMENT
# ======================================================

class Department(models.Model):

    name = models.CharField(max_length=200)

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="departments"
    )

    established_year = models.IntegerField()
    intake = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# ======================================================
# FACULTY
# ======================================================

class Faculty(models.Model):
    faculty_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)

    name = models.CharField(max_length=200)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="faculty"
    )

    qualification = models.CharField(max_length=200)
    is_phd = models.BooleanField(default=False)

    experience_years = models.IntegerField(default=0)

    research_publications = models.IntegerField(default=0)
    patents = models.IntegerField(default=0)
    funded_projects = models.IntegerField(default=0)

    api_score = models.FloatField(default=0)

    def __str__(self):
        return self.name


# ======================================================
# STUDENT
# ======================================================

class Student(models.Model):
    student_uid = models.CharField(max_length=50, unique=True, null=True, blank=True)
    roll_no = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)

    name = models.CharField(max_length=200)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="students"
    )

    year_of_admission = models.IntegerField()
    current_year = models.IntegerField()

    cgpa = models.FloatField(default=0)
    placed = models.BooleanField(default=False)

    mentor = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mentored_students"
    )

    def __str__(self):
        return self.name


# ======================================================
# MENTORSHIP SYSTEM
# ======================================================

class Mentorship(models.Model):

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name="mentorships"
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="mentorships"
    )

    year = models.IntegerField()

    cgpa = models.FloatField(default=0)
    attendance = models.FloatField(default=0)

    risk_level = models.CharField(max_length=20, default="Normal")

    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} - {self.faculty.name}"


# ======================================================
# GOVERNANCE ROLE SYSTEM (OPTIONAL – ADVANCED)
# ======================================================

class GovernanceRole(models.Model):

    ROLE_CHOICES = [
        ("campus_md", "Campus MD"),
        ("campus_director", "Campus Director"),
        ("campus_deputy_director", "Campus Deputy Director"),
        ("admin", "Admin"),
        ("school_dean", "School Dean"),
        ("hod", "Head of Department"),
        ("faculty", "Faculty"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="governance_role"
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    school = models.ForeignKey(
        School,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# ======================================================
# FACULTY PERFORMANCE ENGINE
# ======================================================

class FacultyPerformanceScore(models.Model):

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name="performance_scores"
    )

    year = models.IntegerField(default=timezone.now().year)

    academic_score = models.FloatField(default=0)
    research_score = models.FloatField(default=0)
    student_impact_score = models.FloatField(default=0)
    responsibility_score = models.FloatField(default=0)
    development_score = models.FloatField(default=0)

    total_score = models.FloatField(default=0)
    rank = models.IntegerField(default=0)

    def calculate_scores(self):

        faculty = self.faculty

        academic = min(faculty.api_score / 10, 20)

        research = (
            faculty.research_publications * 2
            + faculty.patents * 5
            + faculty.funded_projects * 4
        )
        research = min(research, 30)

        students = faculty.mentored_students.all()
        total_students = students.count()

        if total_students > 0:
            placed_count = students.filter(placed=True).count()
            placement_rate = (placed_count / total_students) * 20
        else:
            placement_rate = 0

        student_impact = min(placement_rate, 20)

        responsibility = 10 if faculty.is_phd else 5
        responsibility = min(responsibility, 15)

        development = min(faculty.experience_years, 15)

        self.academic_score = academic
        self.research_score = research
        self.student_impact_score = student_impact
        self.responsibility_score = responsibility
        self.development_score = development

        self.total_score = (
            academic + research + student_impact + responsibility + development
        )

    def save(self, *args, **kwargs):
        self.calculate_scores()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.faculty.name} - {self.total_score}"