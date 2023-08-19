from django.db import models
from authentication_app.models import CustomUser
from SubjectSelection.models import Lesson,Unit
from django.utils import timezone


class ProgressTracker(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    completed_units = models.ManyToManyField(Unit, related_name='completed_by', blank=True)
    completed_lessons = models.ManyToManyField(Lesson, related_name='completed_by', blank=True)
    completed_datetime = models.DateTimeField(default=timezone.now)


   