from datetime import timedelta

from django.utils import timezone

from final_project.celery import app
from google_sheets.client import write_to_sheet

from telegram.client import send_telegram_message


@app.task(bind=True)
def vacancy_created_task(self, job_title):
    send_telegram_message(f"Hey! A new vacancy — {job_title} — has just been added🤩")


# @app.task(bind=True)
# def every_second_task(self):
#     print('Every second task!')


@app.task(bind=True)
def everyday_calculation_of_added_vacancies(self):
    from job_hub.models import Vacancy

    # Identify the amount of new vacancies during the day
    end_time = timezone.now().replace(
        hour=10,
        minute=0,
        second=0,
        microsecond=0
    )
    start_time = end_time - timedelta(days=1)

    added_vacancies_during_last_day = Vacancy.objects.filter(
        created_at__range=(start_time, end_time)
    ).count()

    print(
        f"Number of new vacancies during the last day: "
        f"{added_vacancies_during_last_day}"
    )
    send_telegram_message(
        f"Number of new vacancies during the last day: "
        f"{added_vacancies_during_last_day}"
    )


@app.task(bind=True)
def update_google_sheet(self, vacancy_id):
    from job_hub.models import Vacancy

    # Use prefetch_related for ManyToManyField
    vacancy = (
        Vacancy.objects.select_related("category", "salary", "company_profile")
        .prefetch_related("associated_locations")
        .get(id=vacancy_id)
    )

    # Create a list to hold the data for each row
    vacancy_data = []

    # Append data for the vacancy
    vacancy_data.append(
        [
            vacancy.id,
            vacancy.job_title,
            vacancy.category.category_name,
            vacancy.company_profile.company_name,
            vacancy.description,
            vacancy.requirements,
            ", ".join(
                location.location_name
                for location in vacancy.associated_locations.all()
            ),
            str(vacancy.salary),
            vacancy.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        ]
    )

    # Write data to the Google Sheet
    write_to_sheet(vacancy_data)
    return "Done!"
