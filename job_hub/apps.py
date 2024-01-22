from django.apps import AppConfig


class JobHubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'job_hub'

    def ready(self):
        # from job_hub.signals import vacancy_created
        pass
