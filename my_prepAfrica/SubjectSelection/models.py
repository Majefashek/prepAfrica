from django.db import models
from authentication_app.models import CustomUser


class Subjects(models.Model):
    title = models.CharField(blank=True, max_length=50)
    enrolled_user = models.ManyToManyField(CustomUser, blank=True, related_name='enrolled',through="Enrollment"),
    exam_type = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL,),
    

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)


class Unit(models.Model):
    title = models.CharField(blank=True, max_length=50)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='unit_images/', null=True)

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    title = models.CharField(blank=True, max_length=50)
    video_url = models.URLField(blank=True, null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Create your models here.
