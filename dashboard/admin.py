from django.contrib import admin

from .models import (
    Institution,
    School,
    Department,
    Faculty,
    Student,
    GovernanceRole,
    FacultyPerformanceScore,
    Mentorship,
    UserProfile   # 🔥 ADD THIS
)

# =====================================
# CORE STRUCTURE
# =====================================

admin.site.register(Institution)
admin.site.register(School)
admin.site.register(Department)

# =====================================
# USERS & PROFILES
# =====================================

admin.site.register(UserProfile)   # 🔥 IMPORTANT

# =====================================
# ACADEMIC DATA
# =====================================

admin.site.register(Faculty)
admin.site.register(Student)

# =====================================
# GOVERNANCE
# =====================================

admin.site.register(GovernanceRole)
admin.site.register(FacultyPerformanceScore)
admin.site.register(Mentorship)