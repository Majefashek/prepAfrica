# Generated by Django 4.2.2 on 2023-08-05 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SubjectSelection', '0014_remove_lesson_completionstatus_and_more'),
        ('ProgressTrackkingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='progresstracker',
            name='completed_lessons',
            field=models.ManyToManyField(blank=True, related_name='completed_by', to='SubjectSelection.lesson'),
        ),
        migrations.AddField(
            model_name='progresstracker',
            name='completed_units',
            field=models.ManyToManyField(blank=True, related_name='completed_by', to='SubjectSelection.unit'),
        ),
        migrations.AlterField(
            model_name='progresstracker',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
