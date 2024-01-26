from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class Salary(models.Model):
    # salary_range_start = models.DecimalField(max_digits=10, decimal_places=2)
    # salary_range_end = models.DecimalField(max_digits=10, decimal_places=2)
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
        validators=[validate_comma_separated_integer_list],
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
        validators=[validate_comma_separated_integer_list],
    )

    def __str__(self):
        return f"{self.salary_range} {self.currency}"

    class Meta:
        verbose_name_plural = "Salaries"
