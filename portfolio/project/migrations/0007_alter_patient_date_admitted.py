# Generated by Django 4.2.7 on 2023-11-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_patient_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_admitted',
            field=models.DateField(blank=True, null=True),
        ),
    ]
