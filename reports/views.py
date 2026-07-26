from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from .excel_validator import validate_master_template
from .import_engine import import_master_template
from .template_generator import generate_master_template
from .validators import create_upload_log


# =====================================
# DOWNLOAD MASTER TEMPLATE
# =====================================

@login_required
def download_master_template(request):

    excel_file = generate_master_template()

    response = HttpResponse(
        excel_file.getvalue(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="Institutional_Brain_Master_Template.xlsx"'
    )

    return response


# =====================================
# UPLOAD MASTER TEMPLATE
# =====================================

@login_required
def upload_master_template(request):

    if request.method == "POST":

        excel_file = request.FILES.get("file")

        if not excel_file:

            return JsonResponse({
                "status": "error",
                "message": "No file selected."
            })

        errors = validate_master_template(
            excel_file
        )

        if errors:

            create_upload_log(
                user=request.user,
                module="MASTER_TEMPLATE",
                file_name=excel_file.name,
                status="FAILED",
                error_message=str(errors)
            )

            return JsonResponse({
                "status": "error",
                "errors": errors
            })

        import_master_template(
            excel_file
        )

        create_upload_log(
            user=request.user,
            module="MASTER_TEMPLATE",
            file_name=excel_file.name,
            status="SUCCESS"
        )

        return JsonResponse({
            "status": "success",
            "message": "Master Template Imported Successfully."
        })

    return render(
        request,
        "reports/upload_master_template.html"
    )