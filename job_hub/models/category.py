from django.core.exceptions import ValidationError
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

    def save(self, *args, **kwargs):
        # Check if an object with the same category_name already exists
        existing_category = Category.objects.filter(category_name=self.category_name).first()

        if existing_category:
            raise ValidationError("Category with the same name already exists.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_category_name_display()
