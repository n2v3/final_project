# Generated by Django 5.0 on 2024-01-17 15:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("job_hub", "0015_employer_skills"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="vacancy",
            options={
                "ordering": ("-salary",),
                "verbose_name_plural": "Vacancies"
            },
        ),
    ]
