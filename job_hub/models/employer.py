from django.db import models
from .company_profile import CompanyProfile
from .skill import Skill


class Employer(models.Model):
    employer_first_name = models.CharField(max_length=255)
    employer_last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=255)
    company_name = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='employers', null=True,
                                     blank=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.employer_first_name} {self.employer_last_name}"

    class Meta:
        unique_together = ('employer_first_name', 'employer_last_name', 'email', 'company_name')