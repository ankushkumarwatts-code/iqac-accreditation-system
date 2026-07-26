from django.http import HttpResponse


# =========================
# AUTH
# =========================

def login_view(request):
    return HttpResponse("Login Page")


def logout_view(request):
    return HttpResponse("Logout Page")


# =========================
# DASHBOARD
# =========================

def command_center(request):
    return HttpResponse("Command Center Dashboard")


def risk_dashboard(request):
    return HttpResponse("Risk Dashboard")


# =========================
# REPORTS
# =========================

def department_report_pdf(request):
    return HttpResponse("Department Report")


def school_report_pdf(request):
    return HttpResponse("School Report")


def institution_report_pdf(request):
    return HttpResponse("Institution Report")


# =========================
# TEMPLATE DOWNLOAD
# =========================

def download_naac_template(request):
    return HttpResponse("NAAC Template")


def download_nba_template(request):
    return HttpResponse("NBA Template")


def download_faculty_template(request):
    return HttpResponse("Faculty Template")


# =========================
# EXCEL UPLOAD
# =========================

def upload_naac(request):
    return HttpResponse("Upload NAAC")


def upload_nba(request):
    return HttpResponse("Upload NBA")


def upload_faculty(request):
    return HttpResponse("Upload Faculty")


def upload_students(request):
    return HttpResponse("Upload Students")
def demo_dashboard(request):
    from django.shortcuts import render
    return render(request, "demo_dashboard.html")