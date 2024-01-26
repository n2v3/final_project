from django.db import models


class Category(models.Model):
    CATEGORY_CHOICES = [
        ("IT", "Information Technology"),
        ("Healthcare", "Healthcare"),
        ("Finance", "Finance"),
        ("Education", "Education"),
        ("Marketing", "Marketing"),
        ("Engineering", "Engineering"),
        ("Sales", "Sales"),
        ("Customer Service", "Customer Service"),
        ("Retail", "Retail"),
        ("Human Resources", "Human Resources"),
    ]

    category_name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.get_category_name_display()
