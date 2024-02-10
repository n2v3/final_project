from django.db import models
from .company_profile import CompanyProfile


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=255)
    company_name = models.ForeignKey(
        CompanyProfile,
        on_delete=models.CASCADE,
        related_name="employees",
    )
    skills = models.ManyToManyField("Skill")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        unique_together = (
            "first_name", "last_name", "email"
        )
