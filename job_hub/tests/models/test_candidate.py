from django.test import TestCase
from job_hub.models import Candidate, Location, CompanyProfile, Skill

class EmployerModelTest(TestCase):
    def setUp(self):

        # Create a Skill instance for testing
        self.skill = Skill.objects.create(skill_name='Test Skill')

    def test_candidate_creation(self):
        candidate = Candidate.objects.create(
            candidate_first_name='Test candidate first name',
            candidate_last_name='Test candidate last name',
            email='Test Email',
        )

        # Add the Skill to the many-to-many relationship using set()
        candidate.skills.set([self.skill])

        # Check if the object was created successfully
        self.assertIsInstance(candidate, Candidate)

        # Additional assertions
        self.assertEqual(candidate.candidate_first_name, 'Test candidate first name')
        self.assertEqual(candidate.candidate_last_name, 'Test candidate last name')
        self.assertEqual(candidate.email, 'Test Email')
        self.assertEqual(list(candidate.skills.all()), [self.skill])
