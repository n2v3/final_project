from django.test import TestCase
from job_hub.models import CompanyProfile, Location


class EmployerModelTest(TestCase):
    def setUp(self):
        # Create a Location instance for testing
        self.location = Location.objects.create(location_name="Test Location")

    def test_company_profile_creation(self):
        company_profile = CompanyProfile.objects.create(
            company_name="Test Company",
            website="Test website",
            amount_of_employees=2,  # Example value from choices
        )

        # Add the location to the many-to-many relationship using add()
        company_profile.locations.add(self.location)

        # Check if the object was created successfully
        self.assertIsInstance(company_profile, CompanyProfile)

        # Additional assertions
        self.assertEqual(company_profile.company_name, "Test Company")
        self.assertEqual(company_profile.website, "Test website")
        self.assertEqual(company_profile.amount_of_employees, 2)

        # Check if the location is associated with the CompanyProfile
        self.assertIn(self.location, company_profile.locations.all())
