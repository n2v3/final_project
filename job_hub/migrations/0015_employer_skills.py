# Generated by Django 5.0 on 2024-01-14 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job_hub", "0014_alter_employer_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employer",
            name="skills",
            field=models.ManyToManyField(to="job_hub.skill"),
        ),
    ]
