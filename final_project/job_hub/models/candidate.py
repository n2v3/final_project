from django.db import models


class Candidate(models.Model):
    candidate_first_name = models.CharField(max_length=255)
    candidate_last_name = models.CharField(max_length=255)
    email = models.EmailField()
    skills = models.ManyToManyField('Skill')

    class Meta:
        unique_together = ('candidate_first_name', 'candidate_last_name', 'email')

    def get_skills_list(self):
        return self.skills.all()


    def __str__(self):
        return f"{self.candidate_first_name} {self.candidate_last_name}"