import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_project.settings")

app = Celery("final_project")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def hello_world_task(self):
    print("Hello World!")