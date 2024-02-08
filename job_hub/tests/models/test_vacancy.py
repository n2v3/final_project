from django.test import TestCase
from job_hub.models import (
    Vacancy, Location, Category,
    CompanyProfile, Salary, Skill
)


class VacancyModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(location_name="Test Location")
        self.category = Category.objects.create(category_name="Test Category")
        self.company_profile = CompanyProfile.objects.create(
            company_name="Test Company",
            amount_of_employees=2,
        )
        self.company_profile.locations.add(self.location)

        self.salary = Salary.objects.create(salary_range="Test salary range")
        self.skill = Skill.objects.create(skill_name="Test skill")
        self.vacancy = Vacancy.objects.create(
            job_title="Test Job Title",
            description="Test description",
            requirements="Test requirements",
            salary=self.salary,
            company_profile=self.company_profile,
            category=self.category,
        )

    def test_vacancy_creation(self):
        # Add the Location to the many-to-many relationship using add()
        self.vacancy.associated_locations.add(self.location)

        # Add the Skill to the many-to-many relationship using set()
        self.vacancy.skills.set([self.skill])

        # Check if the object was created successfully
        self.assertIsInstance(self.vacancy, Vacancy)

        # Additional assertions
        self.assertEqual(self.vacancy.job_title, "Test Job Title")
        self.assertEqual(self.vacancy.description, "Test description")
        self.assertEqual(self.vacancy.requirements, "Test requirements")
        self.assertEqual(self.vacancy.salary, self.salary)
        self.assertEqual(self.vacancy.company_profile, self.company_profile)
        self.assertEqual(
            list(self.vacancy.associated_locations.all()),
            [self.location]
        )
        self.assertEqual(self.vacancy.category, self.category)
        self.assertEqual(list(self.vacancy.skills.all()), [self.skill])

        self.assertEqual(list(self.location.vacancy_set.all()), [self.vacancy])
        self.assertIn(self.skill, self.vacancy.skills.all())
        self.assertListEqual(list(self.vacancy.skills.all()), [self.skill])

    def test_get_skills_list(self):
        self.vacancy.skills.add(self.skill)  # Add the skill to the vacancy
        skills_list = self.vacancy.get_skills_list()
        self.assertEqual(len(skills_list), 1)
        self.assertEqual(skills_list[0].skill_name, "Test skill")
