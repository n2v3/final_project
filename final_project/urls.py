"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

import job_hub.viewsets as job_hub_viewsets

import job_hub.views as view
from telegram.views import accept_telegram_message

router = DefaultRouter()
router.register(r"candidates", job_hub_viewsets.CandidateViewSet)
router.register(r"employees", job_hub_viewsets.EmployeeViewSet)
router.register(r"employers", job_hub_viewsets.EmployerViewSet)
router.register(r"company-profiles", job_hub_viewsets.CompanyProfileViewSet)
router.register(r"vacancies", job_hub_viewsets.VacancyViewSet)
router.register(r"categories", job_hub_viewsets.CategoryViewSet)
router.register(
    r"comments",
    job_hub_viewsets.CommentViewSet,
    basename="comment"
)
router.register(r"locations", job_hub_viewsets.LocationViewSet)
router.register(r"rates", job_hub_viewsets.RateViewSet, basename="rate")
router.register(r"salaries", job_hub_viewsets.SalaryViewSet)
router.register(r"skills", job_hub_viewsets.SkillViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Job Hub API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", obtain_auth_token),
    path("api/", include(router.urls)),
    path("api/register/", view.registration_view),
    path("telegram/", accept_telegram_message),
    path('api/swagger<format>/',
         schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('api/swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
