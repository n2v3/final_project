from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import Candidate, Employee, Employer, CompanyProfile, Vacancy, Category, Comment, Location, Rate, Salary, Skill
from .serializers import (
    CandidateSerializer, EmployeeSerializer, EmployerSerializer,
    CompanyProfileSerializer, VacancySerializer, CategorySerializer,
    CommentSerializer, LocationSerializer, RateSerializer,
    SalarySerializer, SkillSerializer
)
class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET' or (request.user and request.user.is_authenticated)


class PrivateEndpointMixin:
    permission_classes = [IsAuthenticated]


class CandidateViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Candidate.objects.prefetch_related('skills').all()
    serializer_class = CandidateSerializer


class EmployeeViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('company_name').prefetch_related('skills').all()
    serializer_class = EmployeeSerializer


class EmployerViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Employer.objects.select_related('company_name').prefetch_related('skills').all()
    serializer_class = EmployerSerializer


class CompanyProfileViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.select_related('location').all()
    serializer_class = CompanyProfileSerializer


class VacancyViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Vacancy.objects.select_related('category', 'salary', 'company_profile').prefetch_related('associated_locations', 'skills').all()
    serializer_class = VacancySerializer


class CategoryViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('vacancy').all()
    serializer_class = CommentSerializer


class LocationViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RateViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Rate.objects.select_related('vacancy', 'company_profile').all()
    serializer_class = RateSerializer


class SalaryViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class SkillViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
