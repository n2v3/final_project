from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.category_name