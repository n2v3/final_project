from django.test import TestCase
from job_hub.models import Vacancy, Location, Category, CompanyProfile, Salary, Skill

class TestModelTest(TestCase):
    def setUp(self):

        self.location = Location.objects.create(location_name='Test Location')
        self.category = Category.objects.create(category_name='Test Category')
        self.company_profile = CompanyProfile.objects.create(
            company_name='Test Company',
            amount_of_employees=2,
            location=self.location)
        self.salary = Salary.objects.create(salary_range='Test salary range')
        self.skill = Skill.objects.create(skill_name='Test skill')

    def test_vacancy_creation(self):
        # Check the initial count of Vacancy instances
        initial_count = Vacancy.objects.count()
        # Test creating a Vacancy
        vacancy = Vacancy.objects.create(
            job_title='Test Job Title',
            description='Test description',
            requirements='Test requirements',
            salary=self.salary,
            company_profile=self.company_profile,
            category=self.category,
        )

        # Add the Location to the many-to-many relationship using add()
        vacancy.associated_locations.add(self.location)

        # Add the Skill to the many-to-many relationship using set()
        vacancy.skills.set([self.skill])

        # Check if the object was created successfully
        self.assertIsInstance(vacancy, Vacancy)

        # Additional assertions
        self.assertEqual(vacancy.job_title, 'Test Job Title')
        self.assertEqual(vacancy.description, 'Test description')
        self.assertEqual(vacancy.requirements, 'Test requirements')
        self.assertEqual(vacancy.salary, self.salary)
        self.assertEqual(vacancy.company_profile, self.company_profile)
        self.assertEqual(list(vacancy.associated_locations.all()), [self.location])
        self.assertEqual(vacancy.category, self.category)
        self.assertEqual(list(vacancy.skills.all()), [self.skill])

        # Check if the count of Vacancy instances increased by one
        self.assertEqual(Vacancy.objects.count(), initial_count + 1)

        # Ensure that the Vacancy instance is associated with the correct objects
        self.assertEqual(list(self.location.vacancy_set.all()), [vacancy])
        self.assertIn(self.skill, vacancy.skills.all())
        self.assertListEqual(list(vacancy.skills.all()), [self.skill])