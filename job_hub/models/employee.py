from django.db import models
from .company_profile import CompanyProfile


class Employee(models.Model):
    employee_first_name = models.CharField(max_length=255)
    employee_last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.ForeignKey(
        CompanyProfile,
        on_delete=models.CASCADE,
        related_name="employees",
        null=True,
        blank=True,
    )
    skills = models.ManyToManyField("Skill")

    def __str__(self):
        return f"{self.employee_first_name} {self.employee_last_name}"

    class Meta:
        unique_together = (
            "employee_first_name", "employee_last_name", "email"
        )
