from django.db.models.signals import post_save
from django.dispatch import receiver

from job_hub.models import Vacancy
from job_hub.tasks import vacancy_created_task


@receiver(post_save, sender=Vacancy)
def vacancy_created(sender, instance, **kwargs):
    vacancy_created_task.delay(instance.job_title)
