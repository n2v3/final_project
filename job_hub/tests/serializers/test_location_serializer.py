from django.test import TestCase
from job_hub.models import Location
from job_hub.serializers import LocationSerializer


class LocationSerializerTest(TestCase):
    def setUp(self):
        # Create a sample Location instance for testing
        self.location_data = {"location_name": "Test Location"}
        self.location = Location.objects.create(**self.location_data)

    def test_location_serializer(self):
        # Serialize the Location instance
        serializer = LocationSerializer(instance=self.location)

        # Check the serialized data
        self.assertEqual(
            serializer.data["location_name"],
            self.location_data["location_name"]
        )

    def test_location_deserialization(self):
        # Prepare data for deserialization
        new_location_data = {"location_name": "KYIV"}  # Use a valid choice

        # Deserialize the data
        serializer = LocationSerializer(data=new_location_data)
        serializer.is_valid(raise_exception=True)
        new_location = serializer.save()

        # Check if the new Location instance is created correctly
        self.assertEqual(
            new_location.location_name,
            new_location_data["location_name"]
        )
