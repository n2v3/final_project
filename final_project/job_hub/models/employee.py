from django.db import models


class Employee(models.Model):
    employee_first_name = models.CharField(max_length=255)
    employee_last_name = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.CharField(max_length=255, blank=True, null=True)
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return f"{self.employee_first_name} {self.employee_last_name}"

    class Meta:
        unique_together = ('employee_first_name', 'employee_last_name', 'email')