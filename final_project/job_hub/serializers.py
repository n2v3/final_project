from rest_framework import serializers
from .models import Candidate, Employee, Employer, CompanyProfile, Vacancy, Category, Comment, Location, Rate, Salary, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(slug_field='skill_name', many=True, queryset=Skill.objects.all())

    class Meta:
        model = Candidate
        fields = ('id', 'candidate_first_name', 'candidate_last_name', 'email', 'skills')


class EmployeeSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(slug_field='skill_name', many=True, queryset=Skill.objects.all())

    class Meta:
        model = Employee
        fields = ('employee_first_name', 'employee_last_name', 'email', 'position', 'company_name','skills')


class EmployerSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(slug_field='skill_name', many=True, queryset=Skill.objects.all())

    class Meta:
        model = Employer
        fields = ('employer_first_name', 'employer_last_name', 'email', 'position','company_name', 'skills')

    def get_skills(self, instance):
        return SkillSerializer(instance.skills.all(), many=True).data

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    salary = serializers.SlugRelatedField(slug_field='salary_range', queryset=Salary.objects.all())
    company_profile = serializers.SlugRelatedField(slug_field='company_name',
                                                   queryset=CompanyProfile.objects.all())
    associated_locations = serializers.SlugRelatedField(slug_field='location_name', many=True,
                                                        queryset=Location.objects.all())
    skills = serializers.SlugRelatedField(slug_field='skill_name', many=True, queryset=Skill.objects.all())

    class Meta:
        model = Vacancy
        fields = ('id', 'category', 'job_title', 'description', 'requirements', 'salary', 'company_profile', 'associated_locations', 'skills')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    vacancy = serializers.PrimaryKeyRelatedField(queryset=Vacancy.objects.all())
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Comment
        fields = ('vacancy','comment_text','timestamp')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ('id', 'salary_range', 'currency')
