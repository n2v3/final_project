from django.test import TestCase
from job_hub.models import Salary

class SalaryModelTest(TestCase):
    def test_salary_creation(self):
        # Test creating a Salary instance
        salary = Salary.objects.create(
            salary_range='1000 – 2000',
            currency='EUR'
        )
        # Check if the object was created successfully
        self.assertIsInstance(salary, Salary)

        # Additional assertions
        self.assertEqual(salary.salary_range, '1000 – 2000')
        self.assertEqual(salary.currency, 'EUR')
