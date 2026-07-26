from dashboard.models import School
from .models import DepartmentHealth


class RolePermission:

    CAMPUS_ROLES = [
        "admin",
        "campus_md",
        "campus_director",
        "campus_deputy_director",
    ]

    IQAC_ROLES = [
        "iqac_dean",
        "iqac_deputy_dean",
        "iqac_cell_head",
    ]

    SCHOOL_ROLES = [
        "school_dean",
        "school_principal",
    ]

    HOD_ROLES = [
        "hod",
    ]

    FACULTY_ROLES = [
        "faculty",
    ]


def get_role_scope(profile):

    # -----------------------------
    # Campus Level
    # -----------------------------
    if profile.role in RolePermission.CAMPUS_ROLES:

        return {
            "departments": DepartmentHealth.objects.all().order_by("-health_score"),
            "schools": School.objects.all(),
            "level": "campus",
        }

    # -----------------------------
    # IQAC
    # -----------------------------
    if profile.role in RolePermission.IQAC_ROLES:

        return {
            "departments": DepartmentHealth.objects.all().order_by("-health_score"),
            "schools": School.objects.all(),
            "level": "iqac",
        }

    # -----------------------------
    # School
    # -----------------------------
    if profile.role in RolePermission.SCHOOL_ROLES:

        return {
            "departments": DepartmentHealth.objects.filter(
                department__school=profile.school
            ).order_by("-health_score"),

            "schools": School.objects.filter(
                id=profile.school.id
            ),

            "level": "school",
        }

    # -----------------------------
    # HOD
    # -----------------------------
    if profile.role in RolePermission.HOD_ROLES:

        return {
            "departments": DepartmentHealth.objects.filter(
                department__school=profile.school
            ).order_by("-health_score"),

            "schools": School.objects.filter(
                id=profile.school.id
            ),

            "level": "hod",
        }

    # -----------------------------
    # Faculty
    # -----------------------------
    return {

        "departments": DepartmentHealth.objects.filter(
            department=profile.department
        ),

        "schools": School.objects.none(),

        "level": "faculty",
    }


def is_campus(profile):
    return profile.role in RolePermission.CAMPUS_ROLES


def is_iqac(profile):
    return profile.role in RolePermission.IQAC_ROLES


def is_school(profile):
    return profile.role in RolePermission.SCHOOL_ROLES


def is_hod(profile):
    return profile.role in RolePermission.HOD_ROLES


def is_faculty(profile):
    return profile.role in RolePermission.FACULTY_ROLES