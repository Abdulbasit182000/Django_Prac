# Generated by Django 4.2.7 on 2023-11-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_medicalrecord_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ManyToManyField(related_name='Patients', to='project.doctor'),
        ),
    ]