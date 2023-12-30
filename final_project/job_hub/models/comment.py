from django.db import models
from .employer import Employer
from .employee import Employee
from .candidate import Candidate
from .vacancy import Vacancy


class Comment(models.Model):
    comment_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True)