from django.db import models


class Salary(models.Model):
    salary_range_start = models.DecimalField(max_digits=10, decimal_places=2)
    salary_range_end = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Salaries"