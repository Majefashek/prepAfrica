# Generated by Django 4.2.2 on 2023-07-03 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SubjectSelection', '0002_subjects_enrolled_user_subjects_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='enrolled_user',
        ),
    ]
