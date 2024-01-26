# Generated by Django 5.0 on 2024-01-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job_hub", "0005_alter_category_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyprofile",
            name="amount_of_employees",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Under 100"),
                    (2, "100-500"),
                    (3, "500-1000"),
                    (4, "Above 1000"),
                ]
            ),
        ),
    ]