from django.contrib import admin

from .models import (
    AIReport,
    UploadLog,
    EvidenceRepository,
    ValidationLog,
    ReportActivity,
    Activity,
)

admin.site.register(AIReport)
admin.site.register(UploadLog)
admin.site.register(EvidenceRepository)
admin.site.register(ValidationLog)
admin.site.register(ReportActivity)
admin.site.register(Activity)