from django.db import models
from .company_profile import CompanyProfile


class Employer(models.Model):
    employer_first_name = models.CharField(max_length=255)
    employer_last_name = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.CharField(max_length=255)
    company_profile = models.OneToOneField(CompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employer_first_name} {self.employer_last_name}"

    class Meta:
        unique_together = ('employer_first_name', 'employer_last_name', 'email', 'company_profile')