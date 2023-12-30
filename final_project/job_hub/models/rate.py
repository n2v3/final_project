from django.db import models
from .employer import Employer
from .company_profile import CompanyProfile
from .employee import Employee
from .candidate import Candidate



class Rate(models.Model):
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]

    rating_value = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True)
    company_profile = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, null=True)