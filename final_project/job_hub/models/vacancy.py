from django.db import models
from .company_profile import CompanyProfile
from .location import Location
from .category import Category


class Vacancy(models.Model):
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.ForeignKey('Salary', on_delete=models.CASCADE)
    company_profile = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    associated_locations = models.ManyToManyField(Location)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return f"{self.job_title}"


    class Meta:
        verbose_name_plural = "Vacancies"

    def get_skills_list(self):
        return self.skills.all()