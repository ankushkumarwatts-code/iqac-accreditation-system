# =====================================
# SMART AI REPORT ENGINE
# VERSION 2
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

        objectives = """
1. Bridge the gap between academic learning and industrial practices.
2. Provide practical exposure to students.
3. Improve employability skills.
4. Strengthen industry-academia interaction.
"""

        outcomes = """
1. Students gained practical industrial exposure.
2. Better understanding of real-world processes.
3. Improved professional awareness.
4. Enhanced career readiness.
"""

    elif "seminar" in activity_lower:

        category = "Academic Enrichment Activity"

        objectives = """
1. Enhance academic knowledge.
2. Promote research awareness.
3. Encourage knowledge sharing.
4. Improve analytical thinking.
"""

        outcomes = """
1. Improved subject understanding.
2. Increased research orientation.
3. Better academic interaction.
4. Enhanced learning experience.
"""

    elif "workshop" in activity_lower:

        category = "Skill Development Activity"

        objectives = """
1. Improve practical skills.
2. Enhance technical competency.
3. Promote innovation.
4. Strengthen problem-solving abilities.
"""

        outcomes = """
1. Improved practical knowledge.
2. Enhanced technical skills.
3. Better confidence among participants.
4. Industry readiness improved.
"""

    else:

        category = "Academic Development Activity"

        objectives = """
1. Support holistic development.
2. Improve participation.
3. Enhance institutional quality.
4. Promote continuous learning.
"""

        outcomes = """
1. Better student engagement.
2. Improved academic performance.
3. Positive institutional impact.
4. Enhanced learning culture.
"""

    summary = f"""
The activity '{activity_name}' was organized by the Department of {department}.
The programme was coordinated by {coordinator} and conducted at {venue} on {date}.

A total of {participants} participants actively participated in the event.

The activity contributed towards academic excellence, quality enhancement and institutional development.
"""

    impact_analysis = """
• Enhanced stakeholder engagement.
• Improved learning outcomes.
• Strengthened quality culture.
• Promoted experiential learning.
"""

    naac_mapping = """
Criterion I - Curricular Aspects
Criterion II - Teaching Learning and Evaluation
Criterion III - Research, Innovations and Extension
Criterion V - Student Support and Progression
"""

    nba_mapping = """
PO1 - Engineering Knowledge
PO6 - Society and Sustainability
PO9 - Team Work
PO10 - Communication
PO12 - Life-long Learning
"""

    sdg_mapping = """
SDG 4 - Quality Education
SDG 8 - Decent Work and Economic Growth
SDG 9 - Industry Innovation and Infrastructure
"""

    recommendations = """
1. Conduct similar activities regularly.
2. Increase industry participation.
3. Improve documentation.
4. Enhance outcome assessment.
5. Encourage interdisciplinary involvement.
"""

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