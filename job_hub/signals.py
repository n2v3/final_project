from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def make_user_staff(sender, instance, created, **kwargs):
    if created:
        instance.is_staff = True
        instance.save()
        logger.info(f"User {instance.username} is now staff.")
