from django.db import models

from .vacancy import Vacancy
from .company_profile import CompanyProfile



class Rate(models.Model):
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]

    rating_value = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, default='', related_name='rate')
    company_profile = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, null=True, related_name='rate')