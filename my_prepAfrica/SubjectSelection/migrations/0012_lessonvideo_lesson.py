# Generated by Django 4.2.2 on 2023-07-29 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SubjectSelection', '0011_mylessonvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonvideo',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SubjectSelection.lesson'),
        ),
    ]
