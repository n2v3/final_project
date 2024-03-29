# Generated by Django 5.0 on 2024-01-13 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job_hub", "0010_alter_candidate_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="vacancy",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="job_hub.vacancy",
            ),
        ),
        migrations.AlterField(
            model_name="companyprofile",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="company_profile",
                to="job_hub.location",
            ),
        ),
        migrations.AlterField(
            model_name="rate",
            name="company_profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rate",
                to="job_hub.companyprofile",
            ),
        ),
        migrations.AlterField(
            model_name="rate",
            name="vacancy",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rate",
                to="job_hub.vacancy",
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vacancies",
                to="job_hub.category",
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="company_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vacancies",
                to="job_hub.companyprofile",
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="salary",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vacancies",
                to="job_hub.salary",
            ),
        ),
    ]
