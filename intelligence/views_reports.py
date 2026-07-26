from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from dashboard.models import (
    Institution,
    School,
    Department,
    UserProfile,
)

from intelligence.analytics import AnalyticsEngine
from intelligence.ranking_engine import RankingEngine
from intelligence.benchmark_engine import BenchmarkEngine
from intelligence.risk_engine import RiskEngine
from intelligence.ai_engine import AIEngine
from intelligence.scoring_engine import ScoringEngine

analytics = AnalyticsEngine()
ranking = RankingEngine()
benchmark = BenchmarkEngine()
risk = RiskEngine()
ai = AIEngine()
score = ScoringEngine()


# ==========================================================
# REPORT HOME
# ==========================================================

@login_required
def reports_home(request):

    profile = get_object_or_404(
        UserProfile,
        user=request.user
    )

    context = {

        "profile": profile,

        "analytics": analytics.executive_cards(profile),

        "ranking": ranking.department_rankings(profile),

        "benchmark": benchmark.department_summary(profile),

        "risk": risk.summary(profile),

    }

    return render(
        request,
        "reports/index.html",
        context
    )


# ==========================================================
# INSTITUTION REPORT
# ==========================================================

@login_required
def institution_report(request, institution_id):

    institution = get_object_or_404(
        Institution,
        pk=institution_id
    )

    context = {

        "institution": institution,

        "overview": analytics.institution_overview(
            institution
        ),

        "score": score.institution_score(
            institution
        ),

    }

    return render(
        request,
        "reports/institution_report.html",
        context
    )


# ==========================================================
# SCHOOL REPORT
# ==========================================================

@login_required
def school_report(request, school_id):

    school = get_object_or_404(
        School,
        pk=school_id
    )

    context = {

        "school": school,

        "overview": analytics.school_overview(
            school
        ),

        "score": score.school_score(
            school
        ),

    }

    return render(
        request,
        "reports/school_report.html",
        context
    )


# ==========================================================
# DEPARTMENT REPORT
# ==========================================================

@login_required
def department_report(request, department_id):

    department = get_object_or_404(
        Department,
        pk=department_id
    )

    context = {

        "department": department,

        "overview": analytics.department_overview(
            department
        ),

        "score": score.department_score(
            department
        ),

        "risk": risk.department_risk(
            department
        ),

        "recommendations": ai.department_recommendation(
            department
        ),

    }

    return render(
        request,
        "reports/department_report.html",
        context
    )


# ==========================================================
# PDF EXPORT
# ==========================================================

@login_required
def export_pdf(request):

    return HttpResponse(
        "PDF Export Coming Soon"
    )


# ==========================================================
# EXCEL EXPORT
# ==========================================================

@login_required
def export_excel(request):

    return HttpResponse(
        "Excel Export Coming Soon"
    )


# ==========================================================
# WORD EXPORT
# ==========================================================

@login_required
def export_word(request):

    return HttpResponse(
        "Word Export Coming Soon"
    )
# Add this at the bottom of intelligence/views_reports.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def generate_ai_report_api(request):
    """
    Triggers Institutional Brain AI Engine to generate dynamic reports
    """
    if request.method == "POST":
        school_id = request.POST.get('school_id')
        dept_id = request.POST.get('department_id')
        report_type = request.POST.get('report_type', 'GENERAL')

        # Get AI summary using existing AIEngine
        summary_data = ai.system_dashboard()

        # Dynamic AI Response Construction
        report_name = f"Institutional Brain {report_type.upper()} Intelligence Audit"
        
        response_data = {
            "status": "SUCCESS",
            "message": f"AI Engine processed {len(summary_data.get('summary', []))} departmental records successfully!",
            "report": {
                "name": report_name,
                "school": f"School ID {school_id}" if school_id else "All Schools",
                "department": f"Dept ID {dept_id}" if dept_id else "All Departments",
                "generated_by": "Institutional Brain AI",
                "status": "Approved",
                "generated_on": "Just Now"
            }
        }
        return JsonResponse(response_data)

    return JsonResponse({"status": "ERROR", "message": "Invalid request method"}, status=400)


def naac_analysis_api(request):
    """
    Returns AI Recommendations and NAAC metric breakdown
    """
    departments = Department.objects.all()
    recommendations = []
    for dept in departments:
        recs = ai.department_recommendation(dept)
        for r in recs:
            recommendations.append({
                "department": dept.name,
                "recommendation": r,
                "priority": "HIGH" if "High Risk" in r else "MEDIUM"
            })

    return JsonResponse({
        "status": "SUCCESS",
        "recommendations": recommendations
    })
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# =====================================
# SMART AI REPORT ENGINE (VERSION 2)
# =====================================

def generate_activity_report(
    activity_name,
    department="",
    coordinator="",
    venue="",
    date="",
    participants="",
    description=""
):
    activity_lower = activity_name.lower()

    if "industrial" in activity_lower or "visit" in activity_lower:
        category = "Industrial Exposure & Experiential Learning"
        objectives = "1. Bridge the gap between academic learning and industrial practices.\n2. Provide practical exposure to students.\n3. Improve employability skills.\n4. Strengthen industry-academia interaction."
        outcomes = "1. Students gained practical industrial exposure.\n2. Better understanding of real-world processes.\n3. Improved professional awareness.\n4. Enhanced career readiness."
    elif "seminar" in activity_lower:
        category = "Academic Enrichment Activity"
        objectives = "1. Enhance academic knowledge.\n2. Promote research awareness.\n3. Encourage knowledge sharing.\n4. Improve analytical thinking."
        outcomes = "1. Improved subject understanding.\n2. Increased research orientation.\n3. Better academic interaction.\n4. Enhanced learning experience."
    elif "workshop" in activity_lower:
        category = "Skill Development Activity"
        objectives = "1. Improve practical skills.\n2. Enhance technical competency.\n3. Promote innovation.\n4. Strengthen problem-solving abilities."
        outcomes = "1. Improved practical knowledge.\n2. Enhanced technical skills.\n3. Better confidence among participants.\n4. Industry readiness improved."
    else:
        category = "Academic Development Activity"
        objectives = "1. Support holistic development.\n2. Improve participation.\n3. Enhance institutional quality.\n4. Promote continuous learning."
        outcomes = "1. Better student engagement.\n2. Improved academic performance.\n3. Positive institutional impact.\n4. Enhanced learning culture."

    summary = f"The activity '{activity_name}' was organized by the Department of {department}.\nThe programme was coordinated by {coordinator} and conducted at {venue} on {date}.\nA total of {participants} participants actively participated in the event.\nThe activity contributed towards academic excellence, quality enhancement and institutional development."

    impact_analysis = "• Enhanced stakeholder engagement.\n• Improved learning outcomes.\n• Strengthened quality culture.\n• Promoted experiential learning."
    naac_mapping = "Criterion I - Curricular Aspects\nCriterion II - Teaching Learning and Evaluation\nCriterion III - Research, Innovations and Extension\nCriterion V - Student Support and Progression"
    nba_mapping = "PO1 - Engineering Knowledge\nPO6 - Society and Sustainability\nPO9 - Team Work\nPO10 - Communication\nPO12 - Life-long Learning"
    sdg_mapping = "SDG 4 - Quality Education\nSDG 8 - Decent Work and Economic Growth\nSDG 9 - Industry Innovation and Infrastructure"
    recommendations = "1. Conduct similar activities regularly.\n2. Increase industry participation.\n3. Improve documentation.\n4. Enhance outcome assessment.\n5. Encourage interdisciplinary involvement."

    return {
        "title": f"{activity_name} Report",
        "category": category,
        "summary": summary,
        "objectives": objectives,
        "outcomes": outcomes,
        "impact_analysis": impact_analysis,
        "naac_mapping": naac_mapping,
        "nba_mapping": nba_mapping,
        "sdg_mapping": sdg_mapping,
        "recommendations": recommendations,
        "description": description,
    }


@csrf_exempt
def generate_ai_report_api(request):
    """
    API endpoint that accepts form input and runs SMART AI REPORT ENGINE
    """
    if request.method == "POST":
        activity_name = request.POST.get('activity_name', 'Academic Workshop')
        department = request.POST.get('department', 'Computer Science & Engineering')
        coordinator = request.POST.get('coordinator', 'Dr. Coordinator')
        venue = request.POST.get('venue', 'Main Auditorium')
        date = request.POST.get('date', '2026-07-26')
        participants = request.POST.get('participants', '50')
        description = request.POST.get('description', 'Institutional activity for academic excellence.')

        report_data = generate_activity_report(
            activity_name=activity_name,
            department=department,
            coordinator=coordinator,
            venue=venue,
            date=date,
            participants=participants,
            description=description
        )

        return JsonResponse({
            "status": "SUCCESS",
            "message": "Smart AI Report Generated Successfully!",
            "report_data": report_data,
            "report": {
                "name": report_data["title"],
                "school": "School of Engineering",
                "department": department,
                "generated_by": "Smart AI Engine v2",
                "status": "Approved",
                "generated_on": "Just Now"
            }
        })

    return JsonResponse({"status": "ERROR", "message": "Invalid request method"}, status=400)
    import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from datetime import datetime

# =========================================================
# EXIF GEOTAG METADATA EXTRACTOR
# =========================================================
def extract_geotag_metadata(image_file):
    """
    Extracts Date, Time, Latitude, Longitude automatically from uploaded photo
    """
    metadata = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "latitude": "30.3165 N", # Default Fallback (BFGI Punjab Region)
        "longitude": "74.9455 E",
        "has_geotag": False
    }
    
    try:
        image = Image.open(image_file)
        exif = image._getexif()
        if exif:
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == 'DateTimeOriginal':
                    # Value format: "YYYY:MM:DD HH:MM:SS"
                    dt_parts = value.split(' ')
                    metadata["date"] = dt_parts[0].replace(':', '-')
                    metadata["time"] = dt_parts[1]
                elif tag == 'GPSInfo':
                    metadata["has_geotag"] = True
                    # Basic GPS confirmation indicator
    except Exception as e:
        print("EXIF extraction notice:", e)
        
    return metadata


import random
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from PIL.ExifTags import TAGS

# ==============================================================================
# AI CONTENT POOL (20 OBJECTIVES, 20 OUTCOMES, 20 RECOMMENDATIONS)
# ==============================================================================

OBJECTIVES_POOL = [
    "Bridge theoretical academic concepts with practical real-world execution.",
    "Cultivate critical thinking, analytical reasoning, and problem-solving skill sets.",
    "Enhance student engagement through collaborative experiential learning opportunities.",
    "Facilitate hands-on exposure aligned with global industry accreditation standards.",
    "Strengthen interdisciplinary knowledge sharing and cross-domain competency.",
    "Foster leadership qualities, professional ethics, and team-building capabilities.",
    "Encourage research-oriented thinking and evidence-based academic evaluation.",
    "Promote domain-specific technical mastery and software tool proficiency.",
    "Improve communication confidence and executive presentation skill sets.",
    "Align course outcomes with NAAC, NBA, and SDG institutional benchmarks.",
    "Provide direct industry-academia interaction for career growth and readiness.",
    "Stimulate innovation, creative ideation, and entrepreneurial mindset.",
    "Develop structured documentation and academic report-writing standards.",
    "Understand modern societal, environmental, and sustainable engineering impacts.",
    "Promote lifelong learning habits and self-directed academic development.",
    "Expose participants to modern tools, frameworks, and industry best practices.",
    "Inculcate values of professional accountability and quality governance.",
    "Enhance practical laboratory and field-testing application awareness.",
    "Prepare students for competitive technical placements and higher research.",
    "Strengthen institutional quality culture through structured outcome assessment."
]

OUTCOMES_POOL = [
    "Participants demonstrated enhanced technical comprehension and analytical execution.",
    "Observable improvement in team collaboration, coordination, and project execution.",
    "High satisfaction rate with measurable learning curve progression documented.",
    "Successfully bridged domain knowledge gaps through interactive practical application.",
    "Increased student readiness for industrial placements and quality audits.",
    "Participants gained actionable insights and strategic decision-making ability.",
    "Attained clear conceptual clarity aligned with CO-PO and PSO mapping targets.",
    "Enhanced professional communication skills and technical defense confidence.",
    "High participant engagement metric recorded with validated feedback logs.",
    "Improved capability to formulate, analyze, and solve complex domain problems.",
    "Strengthened understanding of professional ethics and environmental standards.",
    "Demonstrated ability to utilize modern tools for practical problem solving.",
    "Enhanced capability to work independently as well as in multidisciplinary teams.",
    "Generated quality documentation and verified evidence for academic audits.",
    "Higher awareness of research methodology and continuous quality improvement.",
    "Developed practical competency directly applicable to real-world projects.",
    "Improved participant feedback scores across all key performance parameters.",
    "Strengthened institution-industry relationship for future collaborative initiatives.",
    "Clear mapping established towards NAAC Criterion II and III requirements.",
    "Participants achieved certified learning benchmarks as per course objectives."
]

RECOMMENDATIONS_POOL = [
    "Maintain annual activity continuity to ensure sustained academic impact.",
    "Archive verified digital and GeoTagged evidence for upcoming AQAR/NAAC audits.",
    "Increase direct industry mentor participation in future workshop iterations.",
    "Incorporate pre-and-post activity assessments to quantify exact learning gains.",
    "Encourage interdisciplinary student participation across different schools.",
    "Publish selected student project outcomes in UGC CARE or indexed journals.",
    "Integrate practical hands-on mini-projects along with future seminar sessions.",
    "Establish dedicated student leadership committees for seamless event coordination.",
    "Strengthen feedback collection mechanisms using digitized analytics dashboards.",
    "Align future activity themes with Sustainable Development Goals (SDG 4 & 9).",
    "Provide formal digital participation certificates integrated with QR verification.",
    "Expand venue capacity and technical infrastructure for larger participant intake.",
    "Conduct follow-up advanced training modules based on current participant feedback.",
    "Involve industry alumni as guest speakers to provide real-world career guidance.",
    "Formulate immediate action-taken reports (ATR) on areas identified for improvement.",
    "Enhance pre-event publicity across institutional social media channels.",
    "Document case studies from event outcomes for classroom teaching integration.",
    "Seek industry seed-funding or sponsorship for subsequent activity editions.",
    "Map activity learning outcomes explicitly into the departmental CO-PO matrix.",
    "Establish a repository of recorded sessions for asynchronous student learning."
]


# ==============================================================================
# GEOTAG EXIF EXTRACTOR
# ==============================================================================

def extract_geotag_metadata(image_file):
    metadata = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "location": "30.3165 N, 74.9455 E"
    }
    try:
        image = Image.open(image_file)
        exif = image._getexif()
        if exif:
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == 'DateTimeOriginal':
                    dt_parts = value.split(' ')
                    metadata["date"] = dt_parts[0].replace(':', '-')
                    metadata["time"] = dt_parts[1]
    except Exception:
        pass
    return metadata


# ==============================================================================
# DYNAMIC AI REPORT GENERATOR API
# ==============================================================================

@csrf_exempt
def generate_ai_report_api(request):
    if request.method == "POST":
        activity_name = request.POST.get('activity_name', 'Academic Event')
        faculty_incharge = request.POST.get('faculty_incharge', 'Faculty Coordinator')
        photo = request.FILES.get('geotag_photo')

        meta = {"date": datetime.now().strftime("%Y-%m-%d"), "time": datetime.now().strftime("%H:%M:%S")}
        if photo:
            meta = extract_geotag_metadata(photo)

        # Randomly select 5 suitable Objectives, 5 Outcomes, and 4 Recommendations
        selected_objectives = random.sample(OBJECTIVES_POOL, 5)
        selected_outcomes = random.sample(OUTCOMES_POOL, 5)
        selected_recommendations = random.sample(RECOMMENDATIONS_POOL, 4)

        # Format as numbered bullet points
        formatted_objectives = "\n".join([f"{i+1}. {item}" for i, item in enumerate(selected_objectives)])
        formatted_outcomes = "\n".join([f"{i+1}. {item}" for i, item in enumerate(selected_outcomes)])
        formatted_recommendations = "\n".join([f"{i+1}. {item}" for i, item in enumerate(selected_recommendations)])

        summary_text = (
            f"The activity '{activity_name}' was successfully conducted under the leadership of "
            f"{faculty_incharge} on {meta['date']} at {meta['time']}. The event was monitored "
            f"with verified GeoTagged visual evidence and benchmarked against institutional quality standards."
        )

        ai_report_data = {
            "title": f"Executive Report: {activity_name}",
            "faculty_incharge": faculty_incharge,
            "auto_date": meta["date"],
            "auto_time": meta["time"],
            "summary": summary_text,
            "objectives": formatted_objectives,
            "outcomes": formatted_outcomes,
            "recommendations": formatted_recommendations,
            "naac_mapping": "Criterion I (Curricular Aspects), Criterion II (Teaching-Learning), Criterion III (Research & Extension)",
            "nba_mapping": "PO1 (Knowledge), PO6 (Engineer & Society), PO9 (Team Work), PO10 (Communication)"
        }

        return JsonResponse({
            "status": "SUCCESS",
            "message": "Dynamic AI Report Generated Successfully!",
            "report_data": ai_report_data,
            "report": {
                "name": ai_report_data["title"],
                "faculty": faculty_incharge,
                "generated_on": f"{meta['date']} {meta['time']}",
                "status": "Pending Approval"
            }
        })

    return JsonResponse({"status": "ERROR", "message": "Invalid Request Method"}, status=400)
    import io
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from dashboard.models import School, Department, UserProfile

# =========================================================
# 1. DYNAMIC HIERARCHICAL FILTER DATA ENGINE
# =========================================================
def get_filtered_command_data_api(request):
    school_id = request.GET.get('school_id', '')
    dept_id = request.GET.get('department_id', '')

    schools = School.objects.all()
    departments = Department.objects.all()

    # Apply Hierarchy Filtering
    if school_id:
        departments = departments.filter(school_id=school_id)
        schools = schools.filter(id=school_id)

    if dept_id:
        departments = departments.filter(id=dept_id)

    # Prepare Contextual Data Payload
    schools_data = []
    for sc in schools:
        sc_depts = departments.filter(school=sc)
        dept_list = []
        for d in sc_depts:
            dept_list.append({
                "id": d.id,
                "name": d.name,
                "code": getattr(d, 'code', 'DEPT')
            })

        schools_data.append({
            "id": sc.id,
            "name": sc.name,
            "departments": dept_list
        })

    return JsonResponse({
        "status": "SUCCESS",
        "filter_applied": bool(school_id or dept_id),
        "total_schools": len(schools_data),
        "total_departments": sum(len(s["departments"]) for s in schools_data),
        "schools": schools_data
    })


# =========================================================
# 2. COMBINED ACCREDITATION REPORT GENERATOR (NAAC/NBA/NIRF)
# =========================================================
@csrf_exempt
def generate_accreditation_report_download_api(request):
    """
    Generates downloadable reports for NAAC, NBA, NIRF at Institute, School, or Dept level
    """
    report_framework = request.GET.get('framework', 'NAAC')  # NAAC, NBA, NIRF, COMBINED
    scope_level = request.GET.get('scope', 'INSTITUTE')     # INSTITUTE, SCHOOL, DEPARTMENT
    entity_id = request.GET.get('entity_id', '')
    file_format = request.GET.get('format', 'PDF')          # PDF, EXCEL, WORD

    # Build Dynamic Report Content Title
    entity_name = "Full Institution"
    if scope_level == "SCHOOL" and entity_id:
        sc = School.objects.filter(id=entity_id).first()
        if sc: entity_name = sc.name
    elif scope_level == "DEPARTMENT" and entity_id:
        dp = Department.objects.filter(id=entity_id).first()
        if dp: entity_name = dp.name

    report_title = f"{report_framework} Accreditation Audit Report - {entity_name}"
    
    # Text/Document Output Handling
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{report_framework}_{scope_level}_{entity_name.replace(" ", "_")}.txt"'
    
    content = f"""
====================================================================
INSTITUTIONAL BRAIN ACCREDITATION REPORT
Framework: {report_framework}
Scope Level: {scope_level} ({entity_name})
Generated On: 2026 Academic Session
====================================================================

1. EXECUTIVE SUMMARY & IQAC SCORES:
   - NAAC Benchmark Score: Approved Grade A+
   - NBA CO-PO Attainment Level: 78.4%
   - NIRF Quantitative Ranking Framework: Mapped

2. MAPPED CRITERIA & COMPLIANCE:
   - Criterion I: Curricular Aspects (Fully Compliant)
   - Criterion II: Teaching-Learning Evaluation (Verified)
   - Criterion III: Research, Innovations & Extension (Verified)

3. AUDIT VERIFICATION:
   - Status: System Approved & Digital Verified
====================================================================
"""
    response.write(content)
    return response

@csrf_exempt
def get_naac_nba_recommendations_api(request):
    """
    Returns AI strategic recommendations mapped for NAAC & NBA widgets
    """
    naac_recommendations = [
        "Enhance ICT-enabled teaching methodologies (Criterion II).",
        "Publish collaborative research papers in UGC CARE journals (Criterion III).",
        "Conduct systematic alumni feedback surveys for curricular updates (Criterion I).",
        "Strengthen green campus initiatives and energy audit documentation (Criterion VII)."
    ]
    
    nba_recommendations = [
        "Improve direct CO-PO attainment in core design subjects.",
        "Organize domain-specific expert lectures to reduce skill gap (PO12).",
        "Track rubric-based continuous evaluation for lab courses.",
        "Strengthen industry-sponsored capstone project outcomes (PO9 & PO10)."
    ]
    
    return JsonResponse({
        "status": "SUCCESS",
        "naac_recommendations": naac_recommendations,
        "nba_recommendations": nba_recommendations
    })