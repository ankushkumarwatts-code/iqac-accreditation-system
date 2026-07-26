from django.contrib import admin
from .models import Program, Course, CourseOutcome, AttainmentEntry

admin.site.register(Program)
admin.site.register(Course)
admin.site.register(CourseOutcome)
admin.site.register(AttainmentEntry)