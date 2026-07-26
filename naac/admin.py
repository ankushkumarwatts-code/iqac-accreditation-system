from django.contrib import admin
from .models import NAACCriteria, NAACMetric, NAACMetricEntry, NAACExcelUpload


admin.site.register(NAACExcelUpload)
@admin.register(NAACCriteria)
class NAACCriteriaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'weightage')


@admin.register(NAACMetric)
class NAACMetricAdmin(admin.ModelAdmin):
    list_display = ('metric_code', 'criteria', 'max_score')
    list_filter = ('criteria',)


@admin.register(NAACMetricEntry)
class NAACMetricEntryAdmin(admin.ModelAdmin):
    list_display = (
        'metric',
        'school',
        'department',
        'year',
        'achieved_score',
        'target_score'
    )
    list_filter = ('year', 'school', 'department')
