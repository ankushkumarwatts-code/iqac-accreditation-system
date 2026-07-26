import pandas as pd

from reports.models import (
    ValidationLog,
    UploadLog
)


# =====================================
# REQUIRED COLUMN VALIDATION
# =====================================

def validate_required_columns(
    dataframe,
    required_columns
):

    missing = []

    for column in required_columns:

        if column not in dataframe.columns:
            missing.append(column)

    return missing


# =====================================
# SCORE VALIDATION
# =====================================

def validate_score(
    value,
    min_value=0,
    max_value=100
):

    if value < min_value:
        return False

    if value > max_value:
        return False

    return True


# =====================================
# DUPLICATE FILE VALIDATION
# =====================================

def check_duplicate_upload(
    file_name
):

    return UploadLog.objects.filter(
        file_name=file_name
    ).exists()


# =====================================
# VALIDATION LOGGER
# =====================================

def create_validation_log(
    user,
    module,
    issue
):

    ValidationLog.objects.create(
        user=user,
        module=module,
        issue=issue
    )


# =====================================
# UPLOAD LOGGER
# =====================================

def create_upload_log(
    user,
    module,
    file_name,
    department=None,
    status="SUCCESS",
    error_message=""
):

    UploadLog.objects.create(
        user=user,
        module=module,
        file_name=file_name,
        department=department,
        status=status,
        error_message=error_message
    )