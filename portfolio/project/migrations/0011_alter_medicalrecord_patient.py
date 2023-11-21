# Generated by Django 4.2.7 on 2023-11-21 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_remove_book_authors_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='project.patient'),
        ),
    ]
