# Generated by Django 5.0 on 2023-12-30 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("candidate_first_name", models.CharField(max_length=255)),
                ("candidate_last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="CompanyProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=255)),
                ("website", models.URLField()),
                ("amount_of_employees", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("employee_first_name", models.CharField(max_length=255)),
                ("employee_last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Salary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "salary_range_start",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "salary_range_end",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
            options={
                "verbose_name_plural": "Salaries",
            },
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("skill_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Skills",
            },
        ),
        migrations.CreateModel(
            name="Employer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("employer_first_name", models.CharField(max_length=255)),
                ("employer_last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("position", models.CharField(max_length=255)),
                (
                    "company_profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.companyprofile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="companyprofile",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="job_hub.location"
            ),
        ),
        migrations.CreateModel(
            name="Rate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating_value",
                    models.IntegerField(
                        choices=[
                            (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")
                        ]
                    ),
                ),
                ("comment", models.TextField(blank=True, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "candidate",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.candidate",
                    ),
                ),
                (
                    "company_profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.companyprofile",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.employee",
                    ),
                ),
                (
                    "employer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.employer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="employee",
            name="skills",
            field=models.ManyToManyField(to="job_hub.skill"),
        ),
        migrations.AddField(
            model_name="candidate",
            name="skills",
            field=models.ManyToManyField(to="job_hub.skill"),
        ),
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job_title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("requirements", models.TextField()),
                ("associated_locations", models.ManyToManyField(
                    to="job_hub.location"
                )
                 ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.category",
                    ),
                ),
                (
                    "company_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.companyprofile",
                    ),
                ),
                (
                    "salary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.salary"
                    ),
                ),
                ("skills", models.ManyToManyField(to="job_hub.skill")),
            ],
            options={
                "verbose_name_plural": "Vacancies",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment_text", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "candidate",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.candidate",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.employee",
                    ),
                ),
                (
                    "employer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.employer",
                    ),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job_hub.vacancy",
                    ),
                ),
            ],
        ),
    ]
