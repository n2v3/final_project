from django.test import TestCase
from job_hub.models import Candidate, Skill


class CandidateModelTest(TestCase):
    def setUp(self):
        # Create a Skill instance for testing
        self.skill = Skill.objects.create(skill_name="Test Skill")

        # Create a Candidate instance for testing
        self.candidate = Candidate.objects.create(
            candidate_first_name="Test candidate first name",
            candidate_last_name="Test candidate last name",
            email="Test Email",
        )

        # Add the Skill to the many-to-many relationship using set()
        self.candidate.skills.set([self.skill])

    # def test_candidate_creation(self):
    #     # Check if the object was created successfully
    #     self.assertIsInstance(self.candidate, Candidate)
    #
    #     # Additional assertions
    #     self.assertEqual(
    #         self.candidate.candidate_first_name, "Test candidate first name"
    #     )
    #     self.assertEqual(
    #         self.candidate.candidate_last_name,
    #         "Test candidate last name"
    #     )
    #     self.assertEqual(self.candidate.email, "Test Email")
    #     self.assertEqual(list(self.candidate.skills.all()), [self.skill])

    def test_get_skills_list(self):
        # Retrieve the skills list using the get_skills_list method
        skills_list = self.candidate.get_skills_list()

        # Check if the skills list contains the expected skills
        self.assertEqual(len(skills_list), 1)
        self.assertIn(self.skill, skills_list)

    def test_str_representation(self):
        # Test the __str__ method for the Candidate model
        expected_str = "Test candidate first name Test candidate last name"
        self.assertEqual(str(self.candidate), expected_str)
