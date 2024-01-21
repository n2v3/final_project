from datetime import timedelta
from django.utils import timezone

from final_project.celery import app
from job_hub.models import Vacancy
from telegram.client import send_message

@app.task(bind=True)
def vacancy_created_task(self, job_title):
    send_message(f'Hey! A new vacancy — {job_title} — has just been added🤩')


# @app.task(bind=True)
# def every_second_task(self):
#     print('Every second task!')


@app.task(bind=True)
def everyday_calculation_of_added_vacancies(self):
    # Identify the amount of new vacancies during the day
    end_time = timezone.now().replace(hour=10, minute=0, second=0, microsecond=0)
    start_time = end_time - timedelta(days=1)

    added_vacancies_during_last_day = Vacancy.objects.filter(created_at__range=(start_time, end_time)).count()

    print(f"Number of orders during the last day: {added_vacancies_during_last_day}")