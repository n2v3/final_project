from django.core.exceptions import ValidationError
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

    def save(self, *args, **kwargs):
        # Check if an object with the same attributes already exists
        existing_salary = Salary.objects.filter(
            salary_range=self.salary_range,
            currency=self.currency,
        ).first()

        if existing_salary:
            raise ValidationError(
                "Salary with the same range and currency already exists."
            )

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Salaries"
