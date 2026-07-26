from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from intelligence.views import login_view, logout_view


urlpatterns = [

    # ======================================
    # LOGIN PAGE
    # ======================================

    path(
        "",
        login_view,
        name="login"
    ),

    # ======================================
    # LOGOUT
    # ======================================

    path(
        "logout/",
        logout_view,
        name="logout"
    ),

    # ======================================
    # ADMIN PANEL
    # ======================================

    path(
        "admin/",
        admin.site.urls
    ),

    # ======================================
    # MAIN SYSTEM (INSTITUTIONAL BRAIN)
    # ======================================

    path(
        "intelligence/",
        include("intelligence.urls")
    ),
    path("nba/", include("nba.urls")),
    path("naac/", include("naac.urls")),

]


# ======================================
# MEDIA FILES (DEVELOPMENT MODE)
# ======================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )