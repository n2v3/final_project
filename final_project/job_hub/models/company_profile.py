from django.db import models
from .location import Location


class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=255)
    website = models.URLField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    amount_of_employees = models.PositiveIntegerField()

    def __str__(self):
        return self.company_name