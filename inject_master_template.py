import os
import django
import pandas as pd

# 1. Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from dashboard.models import School, Department

# Exact filename from your VS Code sidebar
excel_file = "Institutional_Brain_Master_Template_v1.xlsx"

if not os.path.exists(excel_file):
    print(f"\n❌ ERROR: '{excel_file}' not found in project folder!")
    exit()

print(f"\n📂 Reading Master Template Excel: {excel_file} ...")
xls = pd.ExcelFile(excel_file)

# Dynamic Creator Helper (Safe against missing model fields)
def safe_create_or_get(model_cls, lookup_dict, defaults_dict=None):
    if defaults_dict is None:
        defaults_dict = {}
    
    valid_fields = [f.name for f in model_cls._meta.get_fields() if not f.is_relation or f.many_to_one or f.one_to_one]
    
    clean_lookup = {k: v for k, v in lookup_dict.items() if k in valid_fields and pd.notna(v)}
    clean_defaults = {k: v for k, v in defaults_dict.items() if k in valid_fields and pd.notna(v)}
    
    obj, created = model_cls.objects.get_or_create(**clean_lookup, defaults=clean_defaults)
    
    if not created and clean_defaults:
        for k, v in clean_defaults.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
        obj.save()
    return obj

print("\n🚀 Injecting Data into Database...")

# 1. PROCESS SCHOOLS
if '02_SCHOOLS' in xls.sheet_names:
    df_s = pd.read_excel(xls, '02_SCHOOLS').dropna(subset=['School Name*'], how='all')
    for _, row in df_s.iterrows():
        s_name = str(row['School Name*']).strip()
        if s_name and s_name != 'nan':
            safe_create_or_get(School, {'name': s_name})
    print(f"✔ 02_SCHOOLS Injected. Total Schools in DB: {School.objects.count()}")

# 2. PROCESS DEPARTMENTS
if '03_DEPARTMENTS' in xls.sheet_names:
    df_d = pd.read_excel(xls, '03_DEPARTMENTS').dropna(subset=['Department Name*'], how='all')
    for _, row in df_d.iterrows():
        d_name = str(row['Department Name*']).strip()
        s_name = str(row.get('School Name*', '')).strip()
        
        school_obj = School.objects.filter(name=s_name).first() if s_name else School.objects.first()
            
        if d_name and d_name != 'nan':
            safe_create_or_get(Department, {'name': d_name}, {'school': school_obj})
    print(f"✔ 03_DEPARTMENTS Injected. Total Departments in DB: {Department.objects.count()}")

print("\n🎉 MASTER TEMPLATE EXCEL INJECTED SUCCESSFULLY!")