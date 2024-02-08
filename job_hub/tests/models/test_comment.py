from django.test import TestCase
from job_hub.models import (
    Comment, Vacancy, Category,
    CompanyProfile, Salary, Location
)


class CommentModelTest(TestCase):
    def setUp(self):
        # Create a Location instance for testing
        location = Location.objects.create(location_name="Test Location")

        # Create a Category instance for testing
        category = Category.objects.create(category_name="Test Category")
        company_profile = CompanyProfile.objects.create(
            company_name="Test Company",
            amount_of_employees="1000",
        )
        company_profile.locations.add(location)
        salary = Salary.objects.create(salary_range="Test salary range")

        # Create a Vacancy instance for testing
        self.vacancy = Vacancy.objects.create(
            job_title="Test Vacancy",
            description="Test description",
            requirements="Test requirements",
            # Provide valid instances or IDs for ForeignKey fields
            salary=salary,
            company_profile=company_profile,
            category=category,
        )

    def test_comment_creation(self):
        # Test creating a Comment instance associated with a Vacancy
        comment = Comment.objects.create(
            comment_text="This is a test comment", vacancy=self.vacancy
        )

        # Check if the object was created successfully
        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.comment_text, "This is a test comment")
        self.assertEqual(comment.vacancy, self.vacancy)
