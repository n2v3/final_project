from django.db import models
from .location import Location

class CompanyProfile(models.Model):
    EMPLOYEES_CHOICES = [
        (1, 'Under 100'),
        (2, '100-500'),
        (3, '500-1000'),
        (4, 'Above 1000'),
    ]

    company_name = models.CharField(max_length=255)
    website = models.URLField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    amount_of_employees = models.PositiveIntegerField(choices=EMPLOYEES_CHOICES)

    def __str__(self):
        return self.company_name
