from django.db import models


class Salary(models.Model):
    RANGE_CHOICES = [
        ("UNDER 500", "Under 500"),
        ("500 – 1000", "500 – 1000"),
        ("1000 – 2000", "1000 – 2000"),
        ("2000 – 3500", "2000 – 3500"),
        ("3500 – 5000", "3500 – 5000"),
        ("ABOVE 5000", "Above 5000"),
    ]

    salary_range = models.CharField(
        max_length=20,
        choices=RANGE_CHOICES,
        default="Under 500",
    )

    CURRENCY_CHOICES = [
        ("USD", "US Dollar"),
        ("EUR", "Euro"),
        ("GBP", "British Pound"),
    ]

    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default="USD",
    )

    def __str__(self):
        return f"{self.salary_range} {self.currency}"

    class Meta:
        verbose_name_plural = "Salaries"
