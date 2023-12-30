from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.skill_name