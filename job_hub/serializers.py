from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer, DateTimeField
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


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CompanyProfileSerializer(ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = [
            "id", "company_name", "website",
            "locations", "amount_of_employees"
        ]


class CompanyProfileViewSerializer(CompanyProfileSerializer):
    locations = LocationSerializer()
    # Add a field to show the amount of employees
    amount_of_employees = serializers.CharField(
        source="get_amount_of_employees_display", read_only=True
    )

    def get_amount_of_employees_display(self, obj):
        return obj.get_amount_of_employees_display()


class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = (
            "first_name",
            "last_name",
            "email",
            "position",
            "company_name",
            "skills",
        )


class EmployerViewSerializer(EmployerSerializer):
    company_name = CompanyProfileSerializer()
    skills = SkillSerializer(many=True)


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "employee_first_name",
            "last_name",
            "email",
            "position",
            "company_name",
            "skills",
        )


class EmployeeViewSerializer(EmployeeSerializer):
    company_name = CompanyProfileSerializer()
    skills = SkillSerializer(many=True)


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "skills",
        )


class CandidateViewSerializer(CandidateSerializer):
    skills = SkillSerializer(many=True)


class SalarySerializer(ModelSerializer):
    class Meta:
        model = Salary
        fields = ("id", "salary_range", "currency")


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            "id",
            "category",
            "job_title",
            "description",
            "requirements",
            "salary",
            "company_profile",
            "associated_locations",
            "skills",
        )


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
        fields = ("vacancy", "comment_text", "timestamp")


class CommentViewSerializer(CommentSerializer):
    vacancy = VacancyViewSerializer(read_only=True)


class RateSerializer(serializers.ModelSerializer):
    company_profile = CompanyProfileSerializer(read_only=True)

    class Meta:
        model = Rate
        fields = [
            "id",
            "rating_value",
            "comment",
            "timestamp",
            "vacancy",
            "company_profile",
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token.key

    def create(self, validated_data):
        # Use create_user method to properly trigger signals
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ("username", "password", "token")
