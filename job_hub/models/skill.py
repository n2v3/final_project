from django.core.exceptions import ValidationError
from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Skills"

    def save(self, *args, **kwargs):
        # Check if an object with the same skill_name already exists
        existing_skill = Skill.objects.filter(skill_name=self.skill_name).first()

        if existing_skill:
            raise ValidationError("Skill with the same name already exists.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.skill_name
