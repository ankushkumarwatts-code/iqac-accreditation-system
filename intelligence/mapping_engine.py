from collections import defaultdict

from dashboard.models import (
    Institution,
    School,
    Department,
    Faculty,
    Student,
)

from intelligence.models import (
    DepartmentHealth,
    SchoolHealth,
    InstitutionHealth,
    DepartmentRisk,
)


class MappingEngine:

    """
    ============================================================
    Institutional Brain Enterprise Mapping Engine
    Version : 2.0
    ============================================================

    This engine builds hierarchical relationships between
    Institution → School → Department → Faculty → Student

    Future Parts will add

        • Program Mapping
        • Course Mapping
        • CO Mapping
        • PO Mapping
        • PSO Mapping
        • NAAC Mapping
        • NBA Mapping
        • KPI Mapping
        • AI Mapping
        • Risk Mapping
        • Dashboard Mapping
        • Evidence Mapping
        • Knowledge Graph

    ============================================================
    """

    def __init__(self):

        self.cache = {}

    # ==========================================================
    # Generic Counter
    # ==========================================================

    def _count(self, queryset):

        return queryset.count()

    # ==========================================================
    # Generic List Builder
    # ==========================================================

    def _basic_information(self, obj):

        return {

            "id": obj.id,

            "name": str(obj)

        }

    # ==========================================================
    # Institution Summary
    # ==========================================================

    def institution_summary(self, institution):

        schools = School.objects.filter(
            institution=institution
        )

        departments = Department.objects.filter(
            school__institution=institution
        )

        faculty = Faculty.objects.filter(
            department__school__institution=institution
        )

        students = Student.objects.filter(
            department__school__institution=institution
        )

        health = InstitutionHealth.objects.filter(
            institution=institution
        ).first()

        return {

            "institution": institution,

            "institution_name": institution.name,

            "total_schools": schools.count(),

            "total_departments": departments.count(),

            "total_faculty": faculty.count(),

            "total_students": students.count(),

            "health_score": (
                health.health_score
                if health else 0
            ),

            "schools_queryset": schools,

            "departments_queryset": departments,

            "faculty_queryset": faculty,

            "students_queryset": students,

        }

    # ==========================================================
    # Institution Graph
    # ==========================================================

    def institution_graph(self, institution):

        summary = self.institution_summary(
            institution
        )

        graph = {

            "node": {

                "type": "Institution",

                "id": institution.id,

                "name": institution.name,

            },

            "children": []

        }

        schools = School.objects.filter(
            institution=institution
        ).order_by("name")

        for school in schools:

            graph["children"].append({

                "type": "School",

                "id": school.id,

                "name": school.name,

                "department_count":
                    school.departments.count(),

                "faculty_count":

                    Faculty.objects.filter(

                        department__school=school

                    ).count(),

                "student_count":

                    Student.objects.filter(

                        department__school=school

                    ).count()

            })

        graph["summary"] = summary

        return graph

    # ==========================================================
    # Institution Tree
    # ==========================================================

    def institution_tree(self, institution):

        tree = []

        schools = School.objects.filter(

            institution=institution

        ).order_by("name")

        for school in schools:

            school_node = {

                "school": school,

                "departments": []

            }

            departments = Department.objects.filter(

                school=school

            ).order_by("name")

            for department in departments:

                school_node["departments"].append({

                    "department": department,

                    "faculty": Faculty.objects.filter(

                        department=department

                    ),

                    "students": Student.objects.filter(

                        department=department

                    )

                })

            tree.append(

                school_node

            )

        return tree

    # ==========================================================
    # Institution Statistics
    # ==========================================================

    def institution_statistics(self, institution):

        graph = self.institution_graph(
            institution
        )

        summary = graph["summary"]

        return {

            "institution": institution,

            "schools": summary["total_schools"],

            "departments": summary["total_departments"],

            "faculty": summary["total_faculty"],

            "students": summary["total_students"],

            "health_score": summary["health_score"],

        }

    # ==========================================================
    # (CONTINUED IN PART-2)
    # ==========================================================
        # ==========================================================
    # School Summary
    # ==========================================================

    def school_summary(self, school):

        departments = Department.objects.filter(
            school=school
        )

        faculty = Faculty.objects.filter(
            department__school=school
        )

        students = Student.objects.filter(
            department__school=school
        )

        health = SchoolHealth.objects.filter(
            school=school
        ).first()

        return {

            "school": school,

            "school_name": school.name,

            "institution": school.institution,

            "total_departments": departments.count(),

            "total_faculty": faculty.count(),

            "total_students": students.count(),

            "health_score": (
                health.health_score
                if health else 0
            ),

            "departments_queryset": departments,

            "faculty_queryset": faculty,

            "students_queryset": students,

        }

    # ==========================================================
    # School Graph
    # ==========================================================

    def school_graph(self, school):

        summary = self.school_summary(
            school
        )

        graph = {

            "node": {

                "type": "School",

                "id": school.id,

                "name": school.name,

                "institution": school.institution.name,

            },

            "children": []

        }

        departments = Department.objects.filter(
            school=school
        ).order_by("name")

        for department in departments:

            health = DepartmentHealth.objects.filter(
                department=department
            ).first()

            risk = DepartmentRisk.objects.filter(
                department=department
            ).first()

            graph["children"].append({

                "type": "Department",

                "id": department.id,

                "name": department.name,

                "faculty_count":
                    department.faculty.count(),

                "student_count":
                    department.students.count(),

                "health_score":
                    health.health_score if health else 0,

                "status":
                    health.status if health else "N/A",

                "risk":
                    risk.risk_level if risk else "LOW",

            })

        graph["summary"] = summary

        return graph

    # ==========================================================
    # School Tree
    # ==========================================================

    def school_tree(self, school):

        tree = []

        departments = Department.objects.filter(
            school=school
        ).order_by("name")

        for department in departments:

            tree.append({

                "department": department,

                "faculty":
                    Faculty.objects.filter(
                        department=department
                    ),

                "students":
                    Student.objects.filter(
                        department=department
                    ),

                "faculty_count":
                    Faculty.objects.filter(
                        department=department
                    ).count(),

                "student_count":
                    Student.objects.filter(
                        department=department
                    ).count(),

            })

        return tree

    # ==========================================================
    # School Statistics
    # ==========================================================

    def school_statistics(self, school):

        summary = self.school_summary(
            school
        )

        return {

            "school": school,

            "institution":
                school.institution,

            "departments":
                summary["total_departments"],

            "faculty":
                summary["total_faculty"],

            "students":
                summary["total_students"],

            "health_score":
                summary["health_score"],

        }

    # ==========================================================
    # Department Summary
    # ==========================================================

    def department_summary(self, department):

        faculty = Faculty.objects.filter(
            department=department
        )

        students = Student.objects.filter(
            department=department
        )

        health = DepartmentHealth.objects.filter(
            department=department
        ).first()

        risk = DepartmentRisk.objects.filter(
            department=department
        ).first()

        return {

            "department": department,

            "school": department.school,

            "institution":
                department.school.institution,

            "faculty_queryset": faculty,

            "students_queryset": students,

            "faculty_count": faculty.count(),

            "student_count": students.count(),

            "health_score":
                health.health_score if health else 0,

            "naac_score":
                health.naac_score if health else 0,

            "nba_score":
                health.nba_score if health else 0,

            "status":
                health.status if health else "N/A",

            "risk":
                risk.risk_level if risk else "LOW",

        }

    # ==========================================================
    # CONTINUED IN PART-3
    # ==========================================================
        # ==========================================================
    # Department Graph
    # ==========================================================

    def department_graph(self, department):

        summary = self.department_summary(
            department
        )

        graph = {

            "node": {

                "type": "Department",

                "id": department.id,

                "name": department.name,

                "school": department.school.name,

                "institution":
                    department.school.institution.name,

            },

            "children": []

        }

        faculty = Faculty.objects.filter(
            department=department
        ).order_by("name")

        for member in faculty:

            graph["children"].append({

                "type": "Faculty",

                "id": member.id,

                "name": member.name,

                "designation":
                    getattr(member, "designation", ""),

            })

        students = Student.objects.filter(
            department=department
        ).order_by("name")

        for student in students:

            graph["children"].append({

                "type": "Student",

                "id": student.id,

                "name": student.name,

                "roll_no":
                    getattr(student, "roll_no", ""),

            })

        graph["summary"] = summary

        return graph

    # ==========================================================
    # Department Tree
    # ==========================================================

    def department_tree(self, department):

        return {

            "department": department,

            "faculty": Faculty.objects.filter(
                department=department
            ),

            "students": Student.objects.filter(
                department=department
            ),

            "health": DepartmentHealth.objects.filter(
                department=department
            ).first(),

            "risk": DepartmentRisk.objects.filter(
                department=department
            ).first(),

        }

    # ==========================================================
    # Department Statistics
    # ==========================================================

    def department_statistics(self, department):

        summary = self.department_summary(
            department
        )

        return {

            "department":
                department,

            "faculty":
                summary["faculty_count"],

            "students":
                summary["student_count"],

            "health_score":
                summary["health_score"],

            "naac_score":
                summary["naac_score"],

            "nba_score":
                summary["nba_score"],

            "status":
                summary["status"],

            "risk":
                summary["risk"],

        }

    # ==========================================================
    # Faculty Mapping
    # ==========================================================

    def faculty_mapping(self, department):

        faculty = Faculty.objects.filter(
            department=department
        ).order_by("name")

        return {

            "count": faculty.count(),

            "members": faculty,

            "names": [

                member.name

                for member in faculty

            ],

        }

    # ==========================================================
    # Student Mapping
    # ==========================================================

    def student_mapping(self, department):

        students = Student.objects.filter(
            department=department
        ).order_by("name")

        return {

            "count": students.count(),

            "students": students,

            "names": [

                student.name

                for student in students

            ],

        }

    # ==========================================================
    # Faculty Network
    # ==========================================================

    def faculty_network(self, department):

        network = []

        faculty = Faculty.objects.filter(
            department=department
        )

        for member in faculty:

            network.append({

                "id": member.id,

                "name": member.name,

                "department": department.name,

                "school": department.school.name,

                "institution":
                    department.school.institution.name,

            })

        return network

    # ==========================================================
    # Student Network
    # ==========================================================

    def student_network(self, department):

        network = []

        students = Student.objects.filter(
            department=department
        )

        for student in students:

            network.append({

                "id": student.id,

                "name": student.name,

                "department": department.name,

                "school": department.school.name,

                "institution":
                    department.school.institution.name,

            })

        return network

    # ==========================================================
    # CONTINUED IN PART-4
    # ==========================================================
        # ==========================================================
    # Program Mapping
    # ==========================================================

    def program_mapping(self, department):

        """
        Placeholder for Academics Module.

        Future:
            Program
                ↓
            Semester
                ↓
            Course
        """

        return {

            "department": department,

            "total_programs": 0,

            "programs": [],

            "status": "Program module integration pending"

        }

    # ==========================================================
    # Course Mapping
    # ==========================================================

    def course_mapping(self, department):

        """
        Future Integration

            Department
                ↓
            Courses
                ↓
            Faculty
                ↓
            Students

        """

        return {

            "department": department,

            "total_courses": 0,

            "courses": [],

            "status": "Course module integration pending"

        }

    # ==========================================================
    # Course Network
    # ==========================================================

    def course_network(self, department):

        return {

            "nodes": [],

            "edges": [],

            "department": department

        }

    # ==========================================================
    # Program Network
    # ==========================================================

    def program_network(self, department):

        return {

            "nodes": [],

            "edges": [],

            "department": department

        }

    # ==========================================================
    # CO Mapping
    # ==========================================================

    def co_mapping(self, department):

        """
        NBA Module Integration

        Course Outcomes

        """

        return {

            "department": department,

            "course_outcomes": [],

            "count": 0,

            "status": "Pending"

        }

    # ==========================================================
    # PO Mapping
    # ==========================================================

    def po_mapping(self, department):

        return {

            "department": department,

            "program_outcomes": [],

            "count": 0,

            "status": "Pending"

        }

    # ==========================================================
    # PSO Mapping
    # ==========================================================

    def pso_mapping(self, department):

        return {

            "department": department,

            "program_specific_outcomes": [],

            "count": 0,

            "status": "Pending"

        }

    # ==========================================================
    # CO → PO Mapping
    # ==========================================================

    def co_po_mapping(self, department):

        return {

            "department": department,

            "matrix": [],

            "mapping_strength": 0,

            "status": "Pending NBA Integration"

        }

    # ==========================================================
    # PO → PSO Mapping
    # ==========================================================

    def po_pso_mapping(self, department):

        return {

            "department": department,

            "matrix": [],

            "mapping_strength": 0,

            "status": "Pending"

        }

    # ==========================================================
    # Academic Structure
    # ==========================================================

    def academic_structure(self, department):

        return {

            "department": department,

            "programs": self.program_mapping(department),

            "courses": self.course_mapping(department),

            "course_network": self.course_network(department),

            "program_network": self.program_network(department),

            "co": self.co_mapping(department),

            "po": self.po_mapping(department),

            "pso": self.pso_mapping(department),

            "co_po": self.co_po_mapping(department),

            "po_pso": self.po_pso_mapping(department),

        }

    # ==========================================================
    # CONTINUED IN PART-5
    # ==========================================================
        # ==========================================================
    # NAAC Mapping
    # ==========================================================

    def naac_mapping(self, department):

        health = DepartmentHealth.objects.filter(
            department=department
        ).first()

        return {

            "department": department,

            "naac_score":
                health.naac_score if health else 0,

            "status":
                health.status if health else "N/A",

            "criteria": [],

            "metrics": [],

            "evidence": [],

        }

    # ==========================================================
    # NBA Mapping
    # ==========================================================

    def nba_mapping(self, department):

        health = DepartmentHealth.objects.filter(
            department=department
        ).first()

        return {

            "department": department,

            "nba_score":
                health.nba_score if health else 0,

            "status":
                health.status if health else "N/A",

            "attainment": [],

            "co_po": [],

        }

    # ==========================================================
    # Health Mapping
    # ==========================================================

    def health_mapping(self, department):

        health = DepartmentHealth.objects.filter(
            department=department
        ).first()

        if not health:

            return {

                "health_score": 0,

                "naac_score": 0,

                "nba_score": 0,

                "status": "N/A"

            }

        return {

            "health_score":
                health.health_score,

            "naac_score":
                health.naac_score,

            "nba_score":
                health.nba_score,

            "status":
                health.status,

        }

    # ==========================================================
    # Risk Mapping
    # ==========================================================

    def risk_mapping(self, department):

        risk = DepartmentRisk.objects.filter(
            department=department
        ).first()

        if not risk:

            return {

                "risk_level": "LOW",

                "naac_risk": "LOW",

                "nba_risk": "LOW",

                "issue": ""

            }

        return {

            "risk_level":
                risk.risk_level,

            "naac_risk":
                risk.naac_risk,

            "nba_risk":
                risk.nba_risk,

            "issue":
                risk.issue,

        }

    # ==========================================================
    # KPI Mapping
    # ==========================================================

    def kpi_mapping(self, department):

        health = self.health_mapping(
            department
        )

        risk = self.risk_mapping(
            department
        )

        return {

            "department": department,

            "health_score":
                health["health_score"],

            "naac_score":
                health["naac_score"],

            "nba_score":
                health["nba_score"],

            "risk":
                risk["risk_level"],

            "status":
                health["status"],

        }

    # ==========================================================
    # Dashboard Mapping
    # ==========================================================

    def dashboard_mapping(self, department):

        return {

            "summary":
                self.department_summary(department),

            "statistics":
                self.department_statistics(department),

            "faculty":
                self.faculty_mapping(department),

            "students":
                self.student_mapping(department),

            "health":
                self.health_mapping(department),

            "risk":
                self.risk_mapping(department),

            "kpi":
                self.kpi_mapping(department),

        }

    # ==========================================================
    # CONTINUED IN PART-6
    # ==========================================================
        # ==========================================================
    # Complete Department Graph
    # ==========================================================

    def complete_department_graph(self, department):

        return {

            "summary":
                self.department_summary(department),

            "statistics":
                self.department_statistics(department),

            "graph":
                self.department_graph(department),

            "tree":
                self.department_tree(department),

            "faculty":
                self.faculty_mapping(department),

            "students":
                self.student_mapping(department),

            "faculty_network":
                self.faculty_network(department),

            "student_network":
                self.student_network(department),

            "academics":
                self.academic_structure(department),

            "naac":
                self.naac_mapping(department),

            "nba":
                self.nba_mapping(department),

            "health":
                self.health_mapping(department),

            "risk":
                self.risk_mapping(department),

            "kpi":
                self.kpi_mapping(department),

            "dashboard":
                self.dashboard_mapping(department),

        }

    # ==========================================================
    # School Health Mapping
    # ==========================================================

    def school_health_mapping(self, school):

        health = SchoolHealth.objects.filter(
            school=school
        ).first()

        if not health:
            return {
                "health_score": 0,
                "status": "N/A",
            }

        return {
            "health_score": health.health_score,
            "status": "Available",
        }
    # ==========================================================
    # Complete School Graph
    # ==========================================================

    def complete_school_graph(self, school):

        departments = Department.objects.filter(
            school=school
        ).order_by("name")

        return {

            "summary":
                self.school_summary(school),

            "statistics":
                self.school_statistics(school),

            "graph":
                self.school_graph(school),

            "tree":
                self.school_tree(school),

            "health":
                self.school_health_mapping(school),

            "departments": [

                self.complete_department_graph(
                    department
                )

                for department in departments

            ],

        }

    # ==========================================================
    # CONTINUED IN PART-7
    # ==========================================================
        # ==========================================================
    # Institution Health Mapping
    # ==========================================================

    def institution_health_mapping(self, institution):

        health = InstitutionHealth.objects.filter(
            institution=institution
        ).first()

        if not health:

            return {

                "health_score": 0,

                "status": "N/A"

            }

        return {

            "health_score":
                health.health_score,

            "status":
                health.status,

        }

    # ==========================================================
    # Institution Dashboard Mapping
    # ==========================================================

    def institution_dashboard_mapping(self, institution):

        return {

            "summary":
                self.institution_summary(institution),

            "statistics":
                self.institution_statistics(institution),

            "graph":
                self.institution_graph(institution),

            "tree":
                self.institution_tree(institution),

            "health":
                self.institution_health_mapping(institution),

        }

    # ==========================================================
    # Complete Institution Graph
    # ==========================================================

    def complete_institution_graph(self, institution):

        schools = School.objects.filter(
            institution=institution
        ).order_by("name")

        return {

            "summary":
                self.institution_summary(institution),

            "statistics":
                self.institution_statistics(institution),

            "graph":
                self.institution_graph(institution),

            "tree":
                self.institution_tree(institution),

            "health":
                self.institution_health_mapping(institution),

            "dashboard":
                self.institution_dashboard_mapping(institution),

            "schools": [

                self.complete_school_graph(
                    school
                )

                for school in schools

            ],

        }

    # ==========================================================
    # Search Utilities
    # ==========================================================

    def find_school(self, institution, school_name):

        return School.objects.filter(

            institution=institution,

            name__iexact=school_name

        ).first()

    def find_department(self, school, department_name):

        return Department.objects.filter(

            school=school,

            name__iexact=department_name

        ).first()

    def find_faculty(self, department, faculty_name):

        return Faculty.objects.filter(

            department=department,

            name__iexact=faculty_name

        ).first()

    def find_student(self, department, student_name):

        return Student.objects.filter(

            department=department,

            name__iexact=student_name

        ).first()

    # ==========================================================
    # Counts
    # ==========================================================

    def institution_counts(self, institution):

        return {

            "schools":
                School.objects.filter(
                    institution=institution
                ).count(),

            "departments":
                Department.objects.filter(
                    school__institution=institution
                ).count(),

            "faculty":
                Faculty.objects.filter(
                    department__school__institution=institution
                ).count(),

            "students":
                Student.objects.filter(
                    department__school__institution=institution
                ).count(),

        }

    # ==========================================================
    # CONTINUED IN PART-8
    # ==========================================================
        # ==========================================================
    # Department Counts
    # ==========================================================

    def department_counts(self, department):

        return {

            "faculty":
                Faculty.objects.filter(
                    department=department
                ).count(),

            "students":
                Student.objects.filter(
                    department=department
                ).count(),

        }

    # ==========================================================
    # School Counts
    # ==========================================================

    def school_counts(self, school):

        return {

            "departments":
                Department.objects.filter(
                    school=school
                ).count(),

            "faculty":
                Faculty.objects.filter(
                    department__school=school
                ).count(),

            "students":
                Student.objects.filter(
                    department__school=school
                ).count(),

        }

    # ==========================================================
    # Institution Directory
    # ==========================================================

    def institution_directory(self, institution):

        return {

            "institution": institution,

            "schools": list(
                School.objects.filter(
                    institution=institution
                ).values(
                    "id",
                    "name"
                )
            ),

            "departments": list(
                Department.objects.filter(
                    school__institution=institution
                ).values(
                    "id",
                    "name",
                    "school_id"
                )
            ),

            "faculty": list(
                Faculty.objects.filter(
                    department__school__institution=institution
                ).values(
                    "id",
                    "name",
                    "department_id"
                )
            ),

            "students": list(
                Student.objects.filter(
                    department__school__institution=institution
                ).values(
                    "id",
                    "name",
                    "department_id"
                )
            ),

        }

    # ==========================================================
    # Export Mapping
    # ==========================================================

    def export_mapping(self, institution):

        return {

            "institution":
                self.complete_institution_graph(
                    institution
                ),

            "directory":
                self.institution_directory(
                    institution
                ),

            "counts":
                self.institution_counts(
                    institution
                ),

        }

    # ==========================================================
    # JSON Graph
    # ==========================================================

    def json_graph(self, institution):

        return {

            "type": "InstitutionalBrain",

            "version": "2.0",

            "data":
                self.complete_institution_graph(
                    institution
                )

        }

    # ==========================================================
    # Dashboard API Response
    # ==========================================================

    def dashboard_response(self, institution):

        return {

            "success": True,

            "message":
                "Institution mapping generated successfully.",

            "timestamp": None,

            "result":
                self.complete_institution_graph(
                    institution
                )

        }

    # ==========================================================
    # Cache Management
    # ==========================================================

    def clear_cache(self):

        self.cache = {}

        return True

    def cache_size(self):

        return len(self.cache)

    # ==========================================================
    # Engine Information
    # ==========================================================

    def engine_info(self):

        return {

            "engine":
                "Institutional Brain Enterprise Mapping Engine",

            "version":
                "2.0",

            "author":
                "AK Innovations",

            "supports": [

                "Institution Mapping",
                "School Mapping",
                "Department Mapping",
                "Faculty Mapping",
                "Student Mapping",
                "Academic Structure",
                "NAAC Mapping",
                "NBA Mapping",
                "Health Mapping",
                "Risk Mapping",
                "KPI Mapping",
                "Dashboard Mapping",
                "Institution Graph",
                "School Graph",
                "Department Graph",
                "Export Mapping",
                "JSON Graph"

            ]

        }

    # ==========================================================
    # End of Mapping Engine
    # ==========================================================
    