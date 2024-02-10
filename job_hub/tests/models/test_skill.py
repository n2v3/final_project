from django.test import TestCase

from job_hub.models import Skill


class SkillModelTest(TestCase):
    def test_skill_creation(self):
        # Test creating a Location instance
        skill = Skill.objects.create(skill_name="Analytical thinking")

        # Check if the object was created successfully
        self.assertIsInstance(skill, Skill)
        self.assertEqual(skill.skill_name, "Analytical thinking")

    def test_skill_str_representation(self):
        # Test the __str__ method of the Skill model
        skill = Skill.objects.create(skill_name="Analytical thinking")

        # Check if the __str__ method returns the expected value
        self.assertEqual(str(skill), "Analytical thinking")
