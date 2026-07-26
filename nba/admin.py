from django.contrib import admin
from .models import ProgramOutcome, COPOMapping, NBACriteria, NBAMetric


@admin.register(ProgramOutcome)
class ProgramOutcomeAdmin(admin.ModelAdmin):
    list_display = ('code', 'program')
    list_filter = ('program',)
    search_fields = ('code',)


@admin.register(COPOMapping)
class COPOMappingAdmin(admin.ModelAdmin):
    list_display = ('course_outcome', 'program_outcome', 'mapping_strength')
    list_filter = ('program_outcome__program',)
    search_fields = ('course_outcome__code', 'program_outcome__code')


@admin.register(NBACriteria)
class NBACriteriaAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(NBAMetric)
class NBAMetricAdmin(admin.ModelAdmin):
    list_display = ('title', 'criteria')
    list_filter = ('criteria',)
    search_fields = ('title',)