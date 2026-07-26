from django.contrib import admin

from .models import (
    NIRFYearTarget,
    TLRIndicator,
    RPIndicator,
    GOIndicator,
    OIIndicator,
    PRIndicator,
)

admin.site.register(NIRFYearTarget)
admin.site.register(TLRIndicator)
admin.site.register(RPIndicator)
admin.site.register(GOIndicator)
admin.site.register(OIIndicator)
admin.site.register(PRIndicator)