from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .filters import VacancyFilter
from .models import Candidate, Employee, Employer, CompanyProfile, Vacancy, Category, Comment, Location, Rate, Salary, Skill
from .serializers import (
    CandidateSerializer, EmployeeSerializer, EmployerSerializer,
    CompanyProfileSerializer, VacancySerializer, CategorySerializer,
    CommentSerializer, LocationSerializer, RateSerializer,
    SalarySerializer, SkillSerializer, EmployerViewSerializer, EmployeeViewSerializer, CandidateViewSerializer,
    VacancyViewSerializer, CompanyProfileViewSerializer, CommentViewSerializer
)
from .permissions import MyCustomPermission, ReadOnlyPermission
from .authentication import MyCustomAuthentication
from .tasks import vacancy_created_task


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET' or (request.user and request.user.is_authenticated)


# we wrote the permission class in settings.py, so we don't need this
# class PrivateEndpointMixin:
    # permission_classes = [IsAuthenticated] - Requires that the user making the request is authenticated.
    # If the user is not authenticated, they won't be granted access.
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # If the user is authenticated, they are granted full access (read and write). If the user is not authenticated (anonymous),
    # they are granted read-only access.

    # use like this - class CandidateViewSet(PrivateEndpointMixin, viewsets.ModelViewSet):



class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.prefetch_related('skills').all()
    permission_classes = [MyCustomPermission]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CandidateViewSerializer
        else:
            return CandidateSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('company_name').prefetch_related('skills').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeViewSerializer
        else:
            return EmployeeSerializer

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all().select_related('company_name').prefetch_related('skills').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployerViewSerializer
        else:
            return EmployerSerializer


class CompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.select_related('location').all()
    serializer_class = CompanyProfileSerializer
    authentication_classes = (MyCustomAuthentication,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompanyProfileViewSerializer
        else:
            return CompanyProfileSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.select_related('category', 'salary', 'company_profile').prefetch_related('associated_locations', 'skills').all()
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = VacancyFilter
    search_fields = ['description', 'requirements']
    ordering_fields = ('salary',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VacancyViewSerializer
        else:
            return VacancySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Execute Celery task
        vacancy_created_task.delay(serializer.instance.job_title)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.select_related('vacancy').all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'id'

    # Making request like this http://127.0.0.1:8000/api/comments/?vacancy=5 , we can see the comments regarding specific vacancy
    def get_queryset(self):
        vacancy_id = self.request.query_params.get('vacancy')
        if vacancy_id:
            return Comment.objects.filter(vacancy=vacancy_id)
        else:
            return Comment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentViewSerializer
        else:
            return CommentSerializer

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [ReadOnlyPermission]

class RateViewSet(viewsets.ModelViewSet):
    # queryset = Rate.objects.select_related('vacancy', 'company_profile').all()
    serializer_class = RateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        vacancy_id = self.request.query_params.get('vacancy')
        if vacancy_id:
            return Rate.objects.filter(vacancy=vacancy_id)
        else:
            return Rate.objects.all()


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [ReadOnlyPermission]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('salary_range',)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
