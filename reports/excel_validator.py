import pandas as pd

from reports.template_config import (
    REQUIRED_SHEETS,
    SHEET_COLUMNS
)


# =====================================
# CHECK REQUIRED SHEETS
# =====================================

def validate_sheets(excel_file):

    workbook = pd.ExcelFile(excel_file)

    missing_sheets = []

    for sheet in REQUIRED_SHEETS:

        if sheet not in workbook.sheet_names:
            missing_sheets.append(sheet)

    return missing_sheets


# =====================================
# CHECK REQUIRED COLUMNS
# =====================================

def validate_columns(excel_file):

    workbook = pd.ExcelFile(excel_file)

    errors = []

    for sheet_name, required_columns in SHEET_COLUMNS.items():

        if sheet_name not in workbook.sheet_names:
            continue

        df = pd.read_excel(
            excel_file,
            sheet_name=sheet_name
        )

        for column in required_columns:

            if column not in df.columns:

                errors.append(
                    f"{sheet_name} -> Missing Column: {column}"
                )

    return errors


# =====================================
# EMPTY CELL VALIDATION
# =====================================

def validate_empty_cells(excel_file):

    workbook = pd.ExcelFile(excel_file)

    errors = []

    for sheet_name, required_columns in SHEET_COLUMNS.items():

        if sheet_name not in workbook.sheet_names:
            continue

        df = pd.read_excel(
            excel_file,
            sheet_name=sheet_name
        )

        for column in required_columns:

            if column in df.columns:

                if df[column].isnull().any():

                    errors.append(
                        f"{sheet_name} -> Empty values in {column}"
                    )

    return errors


# =====================================
# FULL MASTER VALIDATION
# =====================================

def validate_master_template(excel_file):

    errors = []

    missing_sheets = validate_sheets(excel_file)

    if missing_sheets:

        for sheet in missing_sheets:

            errors.append(
                f"Missing Sheet: {sheet}"
            )

    column_errors = validate_columns(excel_file)

    errors.extend(column_errors)

    empty_errors = validate_empty_cells(excel_file)

    errors.extend(empty_errors)

    return errors