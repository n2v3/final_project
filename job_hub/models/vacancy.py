from django.db import models
from .company_profile import CompanyProfile
from .location import Location
from .category import Category


class Vacancy(models.Model):
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.ForeignKey('Salary', on_delete=models.CASCADE, related_name='vacancies')
    company_profile = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='vacancies')
    associated_locations = models.ManyToManyField(Location)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.ManyToManyField('Skill')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title}"


    class Meta:
        verbose_name_plural = "Vacancies"
        ordering = ('-salary',)

    def get_skills_list(self):
        return self.skills.all()
