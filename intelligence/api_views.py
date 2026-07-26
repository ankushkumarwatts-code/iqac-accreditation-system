from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from dashboard.models import (
    Institution,
    School,
    Department,
    Faculty,
    Student,
)

from intelligence.models import (
    InstitutionHealth,
    SchoolHealth,
    DepartmentHealth,
    DepartmentRisk,
)

from dashboard.services import DashboardService


service = DashboardService()


# ============================================================
# Dashboard API
# ============================================================

@login_required
def dashboard_api(request):

    context = service.dashboard_context(

        request.user

    )

    return JsonResponse(

        context,

        safe=False

    )


# ============================================================
# Executive Dashboard API
# ============================================================

@login_required
def executive_dashboard_api(request):

    return JsonResponse(

        service.executive_dashboard(),

        safe=False

    )


# ============================================================
# System Report API
# ============================================================

@login_required
def system_report_api(request):

    return JsonResponse(

        service.system_report(),

        safe=False

    )


# ============================================================
# Institution API
# ============================================================

@login_required
def institution_api(request, institution_id):

    institution = get_object_or_404(

        Institution,

        pk=institution_id

    )

    return JsonResponse(

        service.institution_context(

            institution

        ),

        safe=False

    )


# ============================================================
# School API
# ============================================================

@login_required
def school_api(request, school_id):

    school = get_object_or_404(

        School,

        pk=school_id

    )

    return JsonResponse(

        service.school_context(

            school

        ),

        safe=False

    )


# ============================================================
# Department API
# ============================================================

@login_required
def department_api(request, department_id):

    department = get_object_or_404(

        Department,

        pk=department_id

    )

    return JsonResponse(

        service.department_context(

            department

        ),

        safe=False

    )


# ============================================================
# CONTINUED IN PART-2
# ============================================================
# ============================================================
# Faculty API
# ============================================================

@login_required
def faculty_api(request, faculty_id):

    faculty = get_object_or_404(

        Faculty,

        pk=faculty_id

    )

    return JsonResponse(

        {

            "id":
                faculty.id,

            "name":
                faculty.name,

            "department":
                faculty.department.name,

            "school":
                faculty.department.school.name,

            "institution":
                faculty.department.school.institution.name,

        },

        safe=False

    )


# ============================================================
# Student API
# ============================================================

@login_required
def student_api(request, student_id):

    student = get_object_or_404(

        Student,

        pk=student_id

    )

    return JsonResponse(

        {

            "id":
                student.id,

            "name":
                student.name,

            "department":
                student.department.name,

            "school":
                student.department.school.name,

            "institution":
                student.department.school.institution.name,

        },

        safe=False

    )


# ============================================================
# Institution Health API
# ============================================================

@login_required
def institution_health_api(request, institution_id):

    institution = get_object_or_404(

        Institution,

        pk=institution_id

    )

    health = InstitutionHealth.objects.filter(

        institution=institution

    ).values().first()

    return JsonResponse(

        health if health else {},

        safe=False

    )


# ============================================================
# School Health API
# ============================================================

@login_required
def school_health_api(request, school_id):

    school = get_object_or_404(

        School,

        pk=school_id

    )

    health = SchoolHealth.objects.filter(

        school=school

    ).values().first()

    return JsonResponse(

        health if health else {},

        safe=False

    )


# ============================================================
# Department Health API
# ============================================================

@login_required
def department_health_api(request, department_id):

    department = get_object_or_404(

        Department,

        pk=department_id

    )

    health = DepartmentHealth.objects.filter(

        department=department

    ).values().first()

    return JsonResponse(

        health if health else {},

        safe=False

    )


# ============================================================
# Department Risk API
# ============================================================

@login_required
def department_risk_api(request, department_id):

    department = get_object_or_404(

        Department,

        pk=department_id

    )

    risk = DepartmentRisk.objects.filter(

        department=department

    ).values().first()

    return JsonResponse(

        risk if risk else {},

        safe=False

    )


# ============================================================
# CONTINUED IN PART-3
# ============================================================
# ============================================================
# Dashboard Statistics API
# ============================================================

@login_required
def dashboard_statistics_api(request):

    return JsonResponse(

        service.dashboard_statistics(),

        safe=False

    )


# ============================================================
# Health Summary API
# ============================================================

@login_required
def health_summary_api(request):

    return JsonResponse(

        service.health_summary(),

        safe=False

    )


# ============================================================
# Risk Summary API
# ============================================================

@login_required
def risk_summary_api(request):

    return JsonResponse(

        service.risk_summary(),

        safe=False

    )


# ============================================================
# Faculty Summary API
# ============================================================

@login_required
def faculty_summary_api(request):

    return JsonResponse(

        service.faculty_summary(),

        safe=False

    )


# ============================================================
# Student Summary API
# ============================================================

@login_required
def student_summary_api(request):

    return JsonResponse(

        service.student_summary(),

        safe=False

    )


# ============================================================
# Governance Summary API
# ============================================================

@login_required
def governance_summary_api(request):

    return JsonResponse(

        service.governance_summary(),

        safe=False

    )


# ============================================================
# Performance Summary API
# ============================================================

@login_required
def performance_summary_api(request):

    return JsonResponse(

        service.performance_summary(),

        safe=False

    )


# ============================================================
# User Summary API
# ============================================================

@login_required
def user_summary_api(request):

    return JsonResponse(

        service.user_summary(),

        safe=False

    )


# ============================================================
# Quick Statistics API
# ============================================================

@login_required
def quick_statistics_api(request):

    return JsonResponse(

        service.quick_statistics(),

        safe=False

    )


# ============================================================
# CONTINUED IN PART-4
# ============================================================
# ============================================================
# Executive Dashboard API
# ============================================================

@login_required
def executive_dashboard_summary_api(request):

    return JsonResponse(

        service.executive_dashboard(),

        safe=False

    )


# ============================================================
# System Snapshot API
# ============================================================

@login_required
def system_snapshot_api(request):

    return JsonResponse(

        service.system_snapshot(),

        safe=False

    )


# ============================================================
# System Health Report API
# ============================================================

@login_required
def system_health_report_api(request):

    return JsonResponse(

        service.system_health_report(),

        safe=False

    )


# ============================================================
# Institution Directory API
# ============================================================

@login_required
def institution_directory_api(request):

    return JsonResponse(

        service.institution_directory(),

        safe=False

    )


# ============================================================
# Export Dashboard API
# ============================================================

@login_required
def export_dashboard_api(request):

    return JsonResponse(

        service.export_dashboard(

            request.user

        ),

        safe=False

    )


# ============================================================
# Executive Report API
# ============================================================

@login_required
def executive_report_api(request):

    return JsonResponse(

        service.executive_report(),

        safe=False

    )


# ============================================================
# Engine Information API
# ============================================================

@login_required
def engine_information_api(request):

    return JsonResponse(

        service.engine_information(),

        safe=False

    )


# ============================================================
# Search Institution API
# ============================================================

@login_required
def search_institution_api(request):

    keyword = request.GET.get(

        "q",

        ""

    )

    data = list(

        Institution.objects.filter(

            name__icontains=keyword

        ).values(

            "id",

            "name"

        )

    )

    return JsonResponse(

        data,

        safe=False

    )


# ============================================================
# Search School API
# ============================================================

@login_required
def search_school_api(request):

    keyword = request.GET.get(

        "q",

        ""

    )

    data = list(

        School.objects.filter(

            name__icontains=keyword

        ).values(

            "id",

            "name"

        )

    )

    return JsonResponse(

        data,

        safe=False

    )


# ============================================================
# CONTINUED IN PART-5
# ============================================================
# ============================================================
# Search Department API
# ============================================================

@login_required
def search_department_api(request):

    keyword = request.GET.get(

        "q",

        ""

    )

    data = list(

        Department.objects.filter(

            name__icontains=keyword

        ).values(

            "id",

            "name"

        )

    )

    return JsonResponse(

        data,

        safe=False

    )


# ============================================================
# Search Faculty API
# ============================================================

@login_required
def search_faculty_api(request):

    keyword = request.GET.get(

        "q",

        ""

    )

    data = list(

        Faculty.objects.filter(

            name__icontains=keyword

        ).values(

            "id",

            "name"

        )

    )

    return JsonResponse(

        data,

        safe=False

    )


# ============================================================
# Search Student API
# ============================================================

@login_required
def search_student_api(request):

    keyword = request.GET.get(

        "q",

        ""

    )

    data = list(

        Student.objects.filter(

            name__icontains=keyword

        ).values(

            "id",

            "name"

        )

    )

    return JsonResponse(

        data,

        safe=False

    )


# ============================================================
# Institution List API
# ============================================================

@login_required
def institution_list_api(request):

    return JsonResponse(

        list(

            Institution.objects.values(

                "id",

                "name"

            )

        ),

        safe=False

    )


# ============================================================
# School List API
# ============================================================

@login_required
def school_list_api(request):

    return JsonResponse(

        list(

            School.objects.values(

                "id",

                "name",

                "institution_id"

            )

        ),

        safe=False

    )


# ============================================================
# Department List API
# ============================================================

@login_required
def department_list_api(request):

    return JsonResponse(

        list(

            Department.objects.values(

                "id",

                "name",

                "school_id"

            )

        ),

        safe=False

    )


# ============================================================
# Faculty List API
# ============================================================

@login_required
def faculty_list_api(request):

    return JsonResponse(

        list(

            Faculty.objects.values(

                "id",

                "name",

                "department_id"

            )

        ),

        safe=False

    )


# ============================================================
# Student List API
# ============================================================

@login_required
def student_list_api(request):

    return JsonResponse(

        list(

            Student.objects.values(

                "id",

                "name",

                "department_id"

            )

        ),

        safe=False

    )


# ============================================================
# CONTINUED IN PART-6
# ============================================================
# ============================================================
# Institution Count API
# ============================================================

@login_required
def institution_count_api(request):

    return JsonResponse({

        "count":

            Institution.objects.count()

    })


# ============================================================
# School Count API
# ============================================================

@login_required
def school_count_api(request):

    return JsonResponse({

        "count":

            School.objects.count()

    })


# ============================================================
# Department Count API
# ============================================================

@login_required
def department_count_api(request):

    return JsonResponse({

        "count":

            Department.objects.count()

    })


# ============================================================
# Faculty Count API
# ============================================================

@login_required
def faculty_count_api(request):

    return JsonResponse({

        "count":

            Faculty.objects.count()

    })


# ============================================================
# Student Count API
# ============================================================

@login_required
def student_count_api(request):

    return JsonResponse({

        "count":

            Student.objects.count()

    })


# ============================================================
# Dashboard Status API
# ============================================================

@login_required
def dashboard_status_api(request):

    return JsonResponse({

        "status": "running",

        "service": "Institutional Brain",

        "version": "2.0",

    })


# ============================================================
# Ping API
# ============================================================

@login_required
def ping_api(request):

    return JsonResponse({

        "success": True,

        "message": "API Working Successfully"

    })


# ============================================================
# Current User API
# ============================================================

@login_required
def current_user_api(request):

    profile = service.user_profile(

        request.user

    )

    scope = service.user_scope(

        profile

    )

    return JsonResponse({

        "username":

            request.user.username,

        "scope":

            scope,

        "profile":

            str(profile) if profile else None,

    })


# ============================================================
# Dashboard Metadata API
# ============================================================

@login_required
def dashboard_metadata_api(request):

    return JsonResponse({

        "application":

            "Institutional Brain",

        "version":

            "2.0",

        "framework":

            "Django",

        "generated_on":

            str(timezone.now()),

    })


# ============================================================
# CONTINUED IN PART-7
# ============================================================
# ============================================================
# Dashboard Version API
# ============================================================

@login_required
def dashboard_version_api(request):

    return JsonResponse({

        "application":

            "Institutional Brain",

        "module":

            "Dashboard API",

        "version":

            "2.0.0",

        "build":

            "Enterprise",

    })


# ============================================================
# Dashboard Configuration API
# ============================================================

@login_required
def dashboard_configuration_api(request):

    return JsonResponse({

        "analytics": True,

        "ranking": True,

        "kpi": True,

        "benchmark": True,

        "risk": True,

        "ai": True,

        "mapping": True,

        "reports": True,

        "charts": True,

    })


# ============================================================
# Dashboard Modules API
# ============================================================

@login_required
def dashboard_modules_api(request):

    modules = [

        "Institution",

        "School",

        "Department",

        "Faculty",

        "Student",

        "Analytics",

        "Ranking",

        "KPI",

        "Benchmark",

        "Risk",

        "AI",

        "Mapping",

        "Scoring",

        "Health",

    ]

    return JsonResponse(

        {

            "modules": modules,

            "count": len(modules)

        }

    )


# ============================================================
# Dashboard Engines API
# ============================================================

@login_required
def dashboard_engines_api(request):

    engines = [

        "AnalyticsEngine",

        "RankingEngine",

        "KPIEngine",

        "BenchmarkEngine",

        "RiskEngine",

        "AIEngine",

        "MappingEngine",

        "ScoringEngine",

    ]

    return JsonResponse(

        {

            "engines": engines,

            "count": len(engines)

        }

    )


# ============================================================
# Dashboard Services API
# ============================================================

@login_required
def dashboard_services_api(request):

    services = [

        "DashboardService",

        "InstitutionService",

        "SchoolService",

        "DepartmentService",

        "HealthService",

        "RiskService",

        "ExecutiveService",

    ]

    return JsonResponse(

        {

            "services": services,

            "count": len(services)

        }

    )


# ============================================================
# Dashboard Information API
# ============================================================

@login_required
def dashboard_information_api(request):

    return JsonResponse({

        "application":

            "Institutional Brain",

        "organization":

            "AK Innovations",

        "edition":

            "Enterprise",

        "api":

            "v2",

    })


# ============================================================
# End of api_views.py
# ============================================================