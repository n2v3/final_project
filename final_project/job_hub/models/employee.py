from django.db import models


class Employee(models.Model):
    employee_first_name = models.CharField(max_length=255)
    employee_last_name = models.CharField(max_length=255)
    email = models.EmailField()
    skills = models.ManyToManyField('Skill')