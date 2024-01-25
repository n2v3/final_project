from django.test import TestCase
from job_hub.models import Skill
from job_hub.serializers import SkillSerializer

class SkillSerializerTest(TestCase):
    def setUp(self):
        # Create a sample Skill instance for testing
        self.skill_data = {'skill_name': 'Programming'}
        self.skill = Skill.objects.create(**self.skill_data)

    def test_skill_serializer(self):
        # Serialize the Skill instance
        serializer = SkillSerializer(instance=self.skill)

        # Check the serialized data
        self.assertEqual(serializer.data['skill_name'], self.skill_data['skill_name'])

    def test_skill_deserialization(self):
        # Prepare data for deserialization
        new_skill_data = {'skill_name': 'New Skill'}

        # Deserialize the data
        serializer = SkillSerializer(data=new_skill_data)
        serializer.is_valid(raise_exception=True)
        new_skill = serializer.save()

        # Check if the new Skill instance is created correctly
        self.assertEqual(new_skill.skill_name, new_skill_data['skill_name'])
