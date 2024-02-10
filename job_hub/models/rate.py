from django.db import models
from rest_framework.exceptions import ValidationError

from .vacancy import Vacancy


class Rate(models.Model):
    RATING_CHOICES = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]

    rating_value = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name="rate"
    )

    @property
    def company_profile(self):
        return self.vacancy.company_profile

    def save(self, *args, **kwargs):
        # Ensure the rating value is within the allowed choices
        if self.rating_value not in dict(self.RATING_CHOICES).keys():
            raise ValidationError("Invalid rating value")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.rating_value}"
