# Generated by Django 5.0 on 2024-01-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job_hub", "0004_alter_location_location_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="category_name",
            field=models.CharField(
                choices=[
                    ("IT", "Information Technology"),
                    ("Healthcare", "Healthcare"),
                    ("Finance", "Finance"),
                    ("Education", "Education"),
                    ("Marketing", "Marketing"),
                    ("Engineering", "Engineering"),
                    ("Sales", "Sales"),
                    ("Customer Service", "Customer Service"),
                    ("Retail", "Retail"),
                    ("Human Resources", "Human Resources"),
                ],
                max_length=50,
            ),
        ),
    ]
