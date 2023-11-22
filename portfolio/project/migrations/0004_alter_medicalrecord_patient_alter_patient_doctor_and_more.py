# Generated by Django 4.2.7 on 2023-11-13 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0003_remove_patient_doctor_patient_doctor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicalrecord",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Medical_Records",
                to="project.patient",
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="doctor",
            field=models.ManyToManyField(related_name="Doctor_of", to="project.doctor"),
        ),
        migrations.AlterField(
            model_name="patient",
            name="nurse",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Patients",
                to="project.nurse",
            ),
        ),
    ]
