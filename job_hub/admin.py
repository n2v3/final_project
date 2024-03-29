from django.contrib import admin

# Register your models here.

from .models import (
    Candidate,
    Employee,
    Employer,
    CompanyProfile,
    Vacancy,
    Category,
    Comment,
    Location,
    Rate,
    Salary,
    Skill,
)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "position"
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "position"
    )


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'website',
        'display_locations',
        'amount_of_employees'
    )
    ordering = ['company_name', 'amount_of_employees']

    def display_locations(self, obj):
        return ", ".join(
            [
                location.location_name for location in obj.locations.all()
            ]
        )

    display_locations.short_description = 'Locations'


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        "job_title", "description", "requirements", "salary",
        "company_profile", "category"
    )
    search_fields = (
        "job_title",
        "description",
        "salary__salary_range_start",
        "company_profile__company_name",
        "category__category_name",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)
    ordering = ['category_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_text", "timestamp", "vacancy")
    search_fields = ("comment_text", "timestamp", "vacancy__job_title")


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("location_name",)
    search_fields = ("location_name",)
    ordering = ['location_name']


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        "rating_value",
        "comment",
        "timestamp",
        "vacancy",
        "company_profile",
    )
    search_fields = (
        "rating_value",
        "comment",
        "timestamp",
        "vacancy__job_title",
        "company_profile__company_name",
    )


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ("salary_range", "currency")
    search_fields = ("salary_range", "currency")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("skill_name",)
    search_fields = ("skill_name",)
    ordering = ['skill_name']
