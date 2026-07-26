"""
Main Views Router

All business logic is separated into dedicated modules.
"""

from .views_dashboard import *
from .views_reports import *
from .views_upload import *
from .api_views import *

from .auth_views import login_view, logout_view