from django.db.models import Avg
from naac.services import calculate_overall_naac_score
from nba.models import Program, ProgramOutcome
from nba.services import calculate_po_attainment
from .models import Faculty, Student, Department


# =====================================================
# NBA AVERAGE CALCULATION
# =====================================================
def calculate_nba_average(year):
    programs = Program.objects.all()

    total_program_score = 0
    program_count = 0

    for program in programs:
        po_list = ProgramOutcome.objects.filter(program=program)

        total_po_score = 0
        po_count = 0

        for po in po_list:
            attainment = calculate_po_attainment(po, year)
            total_po_score += attainment
            po_count += 1

        if po_count > 0:
            program_score = total_po_score / po_count
            total_program_score += program_score
            program_count += 1

    if program_count == 0:
        return 0

    return round(total_program_score / program_count, 2)


# =====================================================
# INSTITUTIONAL HEALTH INDEX
# =====================================================
def calculate_institutional_health(year):

    naac_score = calculate_overall_naac_score(year)
    nba_score = calculate_nba_average(year)

    health_index = round((naac_score * 0.6) + (nba_score * 0.4), 2)

    return naac_score, nba_score, health_index


# =====================================================
# DEPARTMENT ACADEMIC STRENGTH INDEX
# =====================================================
def calculate_department_strength(department):

    faculty_list = Faculty.objects.filter(department=department)
    student_list = Student.objects.filter(department=department)

    total_faculty = faculty_list.count()
    total_students = student_list.count()

    # 1️⃣ PhD %
    phd_count = faculty_list.filter(is_phd=True).count()
    phd_percent = (phd_count / total_faculty * 100) if total_faculty > 0 else 0

    # 2️⃣ Avg Experience
    avg_experience = faculty_list.aggregate(
        Avg("experience_years")
    )["experience_years__avg"] or 0

    # 3️⃣ Research Score
    total_publications = sum(f.research_publications for f in faculty_list)
    research_score = total_publications / total_faculty if total_faculty > 0 else 0

    # 4️⃣ Student Avg CGPA
    avg_cgpa = student_list.aggregate(
        Avg("cgpa")
    )["cgpa__avg"] or 0

    # 5️⃣ Placement %
    placed_count = student_list.filter(placed=True).count()
    placement_percent = (placed_count / total_students * 100) if total_students > 0 else 0

    # Final Strength Index (Weighted Model)
    strength_index = round(
        (phd_percent * 0.2)
        + (avg_experience * 0.1)
        + (research_score * 0.2)
        + (avg_cgpa * 10 * 0.2)
        + (placement_percent * 0.3),
        2
    )

    return {
        "phd_percent": round(phd_percent, 2),
        "avg_experience": round(avg_experience, 2),
        "research_score": round(research_score, 2),
        "avg_cgpa": round(avg_cgpa, 2),
        "placement_percent": round(placement_percent, 2),
        "strength_index": strength_index,
    }