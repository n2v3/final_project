from django.db import models
from .company_profile import CompanyProfile


class Employer(models.Model):
    employer_first_name = models.CharField(max_length=255)
    employer_last_name = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.CharField(max_length=255)
    company_profile = models.OneToOneField(CompanyProfile, on_delete=models.CASCADE)