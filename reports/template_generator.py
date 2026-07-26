import pandas as pd
from io import BytesIO

from reports.master_template_structure import MASTER_TEMPLATE


def generate_master_template():

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        for sheet_name, columns in MASTER_TEMPLATE.items():

            df = pd.DataFrame(
                columns=columns
            )

            df.to_excel(
                writer,
                sheet_name=sheet_name,
                index=False
            )

    output.seek(0)

    return output