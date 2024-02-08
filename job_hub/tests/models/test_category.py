from django.core.exceptions import ValidationError
from django.test import TestCase

from job_hub.models import Category


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        # Create a Category instance
        category = Category.objects.create(category_name="IT")

        # Check if the Category object is created correctly
        self.assertEqual(category.category_name, "IT")
        self.assertEqual(str(category), "Information Technology")

    def test_save_duplicate_category(self):
        # Create a Category instance with a specific category name
        _ = Category.objects.create(category_name="IT")

        # Try to create another Category with the same category name
        with self.assertRaises(ValidationError):
            Category.objects.create(category_name="IT")

    def test_category_display_name(self):
        category = Category.objects.create(category_name="Finance")

        self.assertEqual(str(category), "Finance")
