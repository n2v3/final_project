# Generated by Django 5.0 on 2024-01-03 16:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("job_hub", "0006_alter_companyprofile_amount_of_employees"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="candidate",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="employee",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="employer",
        ),
    ]
