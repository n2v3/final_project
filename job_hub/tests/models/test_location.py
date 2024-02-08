from django.core.exceptions import ValidationError
from django.test import TestCase

from job_hub.models import Location, CompanyProfile


class LocationModelTest(TestCase):
    def test_location_creation(self):
        # Test creating a Location instance
        location = Location.objects.create(location_name="Kyiv")

        # Check if the object was created successfully
        self.assertIsInstance(location, Location)
        self.assertEqual(location.location_name, "Kyiv")

    def test_save_duplicate_location(self):
        # Create a Location instance with a specific location name
        _ = Location.objects.create(location_name="Kyiv")

        # Try to create another Location with the same location name
        with self.assertRaises(ValidationError):
            Location.objects.create(location_name="Kyiv")

    def test_location_str_representation(self):
        # Test the __str__ method of the Location model
        location = Location.objects.create(location_name="Kharkiv")

        # Check if the __str__ method returns the expected value
        self.assertEqual(str(location), "Kharkiv")

    def test_company_profile_with_locations(self):
        location1 = Location.objects.create(location_name="Kyiv")
        location2 = Location.objects.create(location_name="Kharkiv")

        company_profile = CompanyProfile.objects.create(
            company_name="Test Company",
            website="http://test.com",
            amount_of_employees=1,
        )
        company_profile.locations.add(location1, location2)

        self.assertEqual(company_profile.locations.count(), 2)
        self.assertIn(location1, company_profile.locations.all())
        self.assertIn(location2, company_profile.locations.all())
