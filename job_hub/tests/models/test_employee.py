from django.test import TestCase
from job_hub.models import Employee, Location, CompanyProfile, Skill


class EmployeeModelTest(TestCase):
    def setUp(self):
        # Create a Location instance for testing
        location = Location.objects.create(location_name="Test Location")

        # Create a CompanyProfile instance for testing
        self.company_profile = CompanyProfile.objects.create(
            company_name="Test Company",
            amount_of_employees=1,
        )

        # Add the location to the many-to-many relationship using add()
        self.company_profile.locations.add(location)

        # Create a Skill instance for testing
        self.skill = Skill.objects.create(skill_name="Test Skill")

    def test_employee_creation(self):
        employee = Employee.objects.create(
            employee_first_name="Test employee first name",
            employee_last_name="Test employee last name",
            email="Test Email",
            position="Test Position",
            company_name=self.company_profile,
        )

        # Add the Skill to the many-to-many relationship using set()
        employee.skills.set([self.skill])

        # Check if the object was created successfully
        self.assertIsInstance(employee, Employee)

        # Additional assertions
        self.assertEqual(
            employee.employee_first_name,
            "Test employee first name"
        )
        self.assertEqual(
            employee.employee_last_name,
            "Test employee last name"
        )
        self.assertEqual(employee.email, "Test Email")
        self.assertEqual(employee.position, "Test Position")
        self.assertEqual(employee.company_name, self.company_profile)
        self.assertEqual(list(employee.skills.all()), [self.skill])
