# Generated by Django 4.2.2 on 2023-08-06 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProgressTrackkingApp', '0003_progresstracker_created_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progresstracker',
            old_name='created_datetime',
            new_name='completed_datetime',
        ),
    ]
