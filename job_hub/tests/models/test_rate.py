from django.test import TestCase
from rest_framework.exceptions import ValidationError

from job_hub.models import (
    Rate, Location, Category,
    CompanyProfile, Salary, Vacancy
)


class RateModelTest(TestCase):
    def setUp(self):
        # Create a Location instance for testing
        location = Location.objects.create(location_name="Test Location")

        # Create a Category instance for testing
        category = Category.objects.create(category_name="Test Category")
        company_profile = CompanyProfile.objects.create(
            company_name="Test Company",
            amount_of_employees=4,
        )
        company_profile.locations.add(location)
        salary = Salary.objects.create(salary_range="Test salary range")

        # Create a Vacancy instance for testing
        self.vacancy = Vacancy.objects.create(
            job_title="Test Vacancy",
            description="Test description",
            requirements="Test requirements",
            # Provide valid instances or IDs for ForeignKey fields
            salary=salary,
            company_profile=company_profile,
            category=category,
        )

    def test_rate_creation(self):
        # Test creating a Rate instance associated with a Vacancy
        rate = Rate.objects.create(rating_value=5, vacancy=self.vacancy)

        # Check if the object was created successfully
        self.assertIsInstance(rate, Rate)
        self.assertEqual(rate.rating_value, 5)
        self.assertEqual(rate.vacancy, self.vacancy)

    def test_rate_creation_with_invalid_rating(self):
        # Test creating a Rate instance with an invalid rating value (> 5)
        with self.assertRaises(ValidationError):
            Rate.objects.create(rating_value=6, vacancy=self.vacancy)
