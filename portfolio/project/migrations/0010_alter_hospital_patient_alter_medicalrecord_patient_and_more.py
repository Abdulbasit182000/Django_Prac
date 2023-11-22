# Generated by Django 4.2.7 on 2023-11-17 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0009_remove_author_headshot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hospital",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="hospitals",
                to="project.patient",
            ),
        ),
        migrations.AlterField(
            model_name="medicalrecord",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="records",
                to="project.patient",
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="doctor",
            field=models.ManyToManyField(related_name="patients", to="project.doctor"),
        ),
        migrations.AlterField(
            model_name="patient",
            name="nurse",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patients",
                to="project.nurse",
            ),
        ),
    ]
