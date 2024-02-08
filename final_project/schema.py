import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from job_hub.models import (
    Vacancy, CompanyProfile, Location, Category, Salary,
    Skill, Rate, Employer, Employee, Comment, Candidate
)


class EmployerNode(DjangoObjectType):
    class Meta:
        model = Employer
        filter_fields = ['employer_first_name', 'employer_last_name', 'email']
        interfaces = (relay.Node,)


class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = ['employee_first_name', 'employee_last_name', 'email']
        interfaces = (relay.Node,)


class CandidateNode(DjangoObjectType):
    class Meta:
        model = Candidate
        filter_fields = [
            'candidate_first_name',
            'candidate_last_name',
            'email'
        ]
        interfaces = (relay.Node,)


class SalaryNode(DjangoObjectType):
    class Meta:
        model = Salary
        filter_fields = {
            'salary_range': ['exact'],
            'currency': ['exact'],
        }
        interfaces = (relay.Node,)


class CompanyProfileNode(DjangoObjectType):
    class Meta:
        model = CompanyProfile
        filter_fields = {
            'company_name': ['exact', 'icontains', 'istartswith'],
            'website': ['exact', 'icontains', 'istartswith'],
            'locations': ['exact'],
            'amount_of_employees': ['exact'],
        }
        interfaces = (relay.Node,)


class LocationNode(DjangoObjectType):
    class Meta:
        model = Location
        filter_fields = {
            'location_name': ['exact'],
        }
        interfaces = (relay.Node,)


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            'category_name': ['exact'],
        }
        interfaces = (relay.Node,)


class SkillNode(DjangoObjectType):
    class Meta:
        model = Skill
        filter_fields = {
            'skill_name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)


class VacancyNode(DjangoObjectType):
    class Meta:
        model = Vacancy
        filter_fields = {
            'job_title': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'requirements': ['exact', 'icontains', 'istartswith'],
            'salary': ['exact'],
            'company_profile': ['exact'],
            'associated_locations': ['exact'],
            'category': ['exact'],
            'skills': ['exact'],
            'created_at': ['exact', 'gte', 'lte'],
        }
        interfaces = (relay.Node,)


class RateNode(DjangoObjectType):
    class Meta:
        model = Rate
        filter_fields = ['rating_value', 'vacancy']
        interfaces = (relay.Node,)


class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        filter_fields = ['vacancy']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    employer = relay.Node.Field(EmployerNode)
    all_employers = DjangoFilterConnectionField(EmployerNode)

    employee = relay.Node.Field(EmployeeNode)
    all_employees = DjangoFilterConnectionField(EmployeeNode)

    candidate = relay.Node.Field(CandidateNode)
    all_candidates = DjangoFilterConnectionField(CandidateNode)

    salary = relay.Node.Field(SalaryNode)
    all_salaries = DjangoFilterConnectionField(SalaryNode)

    company_profile = relay.Node.Field(CompanyProfileNode)
    all_company_profiles = DjangoFilterConnectionField(CompanyProfileNode)

    location = relay.Node.Field(LocationNode)
    all_locations = DjangoFilterConnectionField(LocationNode)

    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    skill = relay.Node.Field(SkillNode)
    all_skills = DjangoFilterConnectionField(SkillNode)

    vacancy = relay.Node.Field(VacancyNode)
    all_vacancies = DjangoFilterConnectionField(VacancyNode)

    rate = relay.Node.Field(RateNode)
    all_rates = DjangoFilterConnectionField(RateNode)

    comment = relay.Node.Field(CommentNode)
    all_comments = DjangoFilterConnectionField(CommentNode)


schema = graphene.Schema(query=Query)
