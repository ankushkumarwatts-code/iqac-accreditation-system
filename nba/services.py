from .models import COPOMapping, ProgramOutcome
from academics.models import AttainmentEntry


def calculate_po_attainment(program_outcome, year):
    """
    Calculate PO attainment using:
    CO attainment × mapping_strength
    """

    mappings = COPOMapping.objects.filter(program_outcome=program_outcome)

    total_weighted_score = 0
    total_mapping_strength = 0

    for mapping in mappings:
        try:
            attainment_entry = AttainmentEntry.objects.get(
                course_outcome=mapping.course_outcome,
                year=year
            )
            co_attainment = attainment_entry.attainment_percentage
        except AttainmentEntry.DoesNotExist:
            co_attainment = 0

        total_weighted_score += co_attainment * mapping.mapping_strength
        total_mapping_strength += mapping.mapping_strength

    if total_mapping_strength == 0:
        return 0

    return round(total_weighted_score / total_mapping_strength, 2)