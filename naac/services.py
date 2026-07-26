from .models import NAACCriteria, NAACMetricEntry
from dashboard.models import School


# =========================
# CRITERIA PERCENTAGE
# =========================
def calculate_criteria_percentage(criteria, year, school=None, department=None):
    entries = NAACMetricEntry.objects.filter(
        metric__criteria=criteria,
        year=year
    )

    if department:
        entries = entries.filter(department=department)
    elif school:
        entries = entries.filter(school=school)

    total_achieved = sum(e.achieved_score for e in entries)
    total_target = sum(e.target_score for e in entries)

    if total_target == 0:
        return 0

    return round((total_achieved / total_target) * 100, 2)


# =========================
# OVERALL NAAC SCORE
# =========================
def calculate_overall_naac_score(year, school=None, department=None):
    criteria_list = NAACCriteria.objects.all()

    total_weighted_score = 0
    total_weight = 0

    for criteria in criteria_list:
        percentage = calculate_criteria_percentage(
            criteria,
            year,
            school=school,
            department=department
        )

        weighted_score = (percentage / 100) * criteria.weightage

        total_weighted_score += weighted_score
        total_weight += criteria.weightage

    if total_weight == 0:
        return 0

    return round((total_weighted_score / total_weight) * 100, 2)


# =========================
# SCHOOL COMPARISON
# =========================
def calculate_school_comparison(year):
    schools = School.objects.all()
    school_data = []

    for school in schools:
        score = calculate_overall_naac_score(year, school=school)

        school_data.append({
            "name": school.name,
            "score": score
        })

    return school_data


# =========================
# SCHOOL YEARLY TREND
# =========================
def calculate_school_yearly_trend(years):
    schools = School.objects.all()
    result = []

    for school in schools:
        yearly_scores = []

        for year in years:
            score = calculate_overall_naac_score(year, school=school)
            yearly_scores.append(score)

        result.append({
            "school": school.name,
            "scores": yearly_scores
        })

    return result