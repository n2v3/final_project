from django.test import TestCase
from job_hub.models import Employer, Location, CompanyProfile, Skill


class EmployerModelTest(TestCase):
    def setUp(self):
        # Create a Location instance for testing
        location = Location.objects.create(location_name="Test Location")

        # Create a CompanyProfile instance for testing
        self.company_profile = CompanyProfile.objects.create(
            company_name="Test Company",
            amount_of_employees=3,
        )

        # Add the location to the many-to-many relationship using add()
        self.company_profile.locations.add(location)

        # Create a Skill instance for testing
        self.skill = Skill.objects.create(skill_name="Test Skill")

    def test_employer_creation(self):
        employer = Employer.objects.create(
            first_name="Test first name",
            last_name="Test last name",
            email="Test Email",
            position="Test Position",
            company_name=self.company_profile,
        )

        # Add the Skill to the many-to-many relationship using set()
        employer.skills.set([self.skill])

        # Check if the object was created successfully
        self.assertIsInstance(employer, Employer)

        # Additional assertions
        self.assertEqual(
            employer.first_name,
            "Test first name"
        )
        self.assertEqual(
            employer.last_name,
            "Test last name"
        )
        self.assertEqual(employer.email, "Test Email")
        self.assertEqual(employer.position, "Test Position")
        self.assertEqual(employer.company_name, self.company_profile)
        self.assertEqual(list(employer.skills.all()), [self.skill])
