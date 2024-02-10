from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    skills = models.ManyToManyField("Skill")

    def get_skills_list(self):
        return self.skills.all()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
