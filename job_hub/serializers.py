from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, DateTimeField, SerializerMethodField
from .models import Candidate, Employee, Employer, CompanyProfile, Vacancy, Category, Comment, Location, Rate, Salary, \
    Skill

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CompanyProfileSerializer(ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = ['id', 'company_name', 'website', 'location', 'amount_of_employees']

class CompanyProfileViewSerializer(CompanyProfileSerializer):
    location = LocationSerializer()
    # Add a field to show the amount of employees
    amount_of_employees = serializers.CharField(source='get_amount_of_employees_display', read_only=True)

    def get_amount_of_employees_display(self, obj):
        # Get the display value for the amount of employees based on the model choices
        return obj.get_amount_of_employees_display()


class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = ('employer_first_name', 'employer_last_name', 'email', 'position', 'company_name', 'skills')

class EmployerViewSerializer(EmployerSerializer):
    company_name = CompanyProfileSerializer()
    skills = SkillSerializer(many=True)

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_first_name', 'employee_last_name', 'email', 'position', 'company_name','skills')

class EmployeeViewSerializer(EmployeeSerializer):
    company_name = CompanyProfileSerializer()
    skills = SkillSerializer(many=True)

class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'candidate_first_name', 'candidate_last_name', 'email', 'skills')

class CandidateViewSerializer(CandidateSerializer):
    skills = SkillSerializer(many=True)


class SalarySerializer(ModelSerializer):
    class Meta:
        model = Salary
        fields = ('id', 'salary_range', 'currency')

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'category', 'job_title', 'description', 'requirements', 'salary', 'company_profile', 'associated_locations', 'skills')

class VacancyViewSerializer(VacancySerializer):
    skills = SkillSerializer(many=True)
    associated_locations = LocationSerializer(many=True)
    company_profile = CompanyProfileSerializer()
    category = CategorySerializer()
    salary = SalarySerializer()

class CommentSerializer(ModelSerializer):
    # vacancy = PrimaryKeyRelatedField(queryset=Vacancy.objects.all())
    timestamp = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Comment
        fields = ('vacancy','comment_text','timestamp')

class CommentViewSerializer(CommentSerializer):
    vacancy = VacancyViewSerializer(read_only=True)


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ('username', 'password', 'token')

