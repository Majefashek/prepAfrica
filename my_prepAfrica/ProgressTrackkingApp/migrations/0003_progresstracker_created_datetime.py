# Generated by Django 4.2.2 on 2023-08-06 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProgressTrackkingApp', '0002_progresstracker_completed_lessons_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='progresstracker',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
