from django.core.exceptions import ValidationError
from django.test import TestCase
from job_hub.models import Salary


class SalaryModelTest(TestCase):
    def test_salary_creation(self):
        # Test creating a Salary instance
        salary = Salary.objects.create(
            salary_range="1000 – 2000",
            currency="EUR"
        )
        # Check if the object was created successfully
        self.assertIsInstance(salary, Salary)

        # Additional assertions
        self.assertEqual(salary.salary_range, "1000 – 2000")
        self.assertEqual(salary.currency, "EUR")

    def test_save_duplicate_salary(self):
        # Create a Salary instance with a specific salary range and currency
        salary = Salary.objects.create(
            salary_range="3500 – 5000",
            currency="GBP"
        )

        # Try to create another Salary with the same range and currency
        with self.assertRaises(ValidationError):
            Salary.objects.create(
                salary_range="3500 – 5000",
                currency="GBP"
            )
