from django.db import models
from authentication_app.models import CustomUser
#from ProgressTrackkingApp.models import ProgressTracker
from django.utils import timezone


class Subjects(models.Model):
    title = models.CharField(blank=True, max_length=50)
    enrolled_user = models.ManyToManyField(CustomUser, blank=True, related_name='enrolled',through="Enrollment"),
    exam_type = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL,),
    

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)


class Unit(models.Model):
    title = models.CharField(blank=True, max_length=50)
    subject = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    image = models.ImageField(blank=True, upload_to='unit_images/', null=True)
    #progress=models.ForeignKey(ProgressTracker, on_delete=models.CASCADE,null=True,blank=True)
    

    

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    title = models.CharField(blank=True, max_length=50)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING,default=True)
    #progress=models.ForeignKey(ProgressTracker, on_delete=models.CASCADE,null=True,blank=True)
    
   
    def __str__(self):
        return self.title
    
class LessonVideo(models.Model):
    title=models.CharField(max_length=50)
    video_url = models.URLField(blank=True, null=True)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE,null=True,blank=True,)

class MyLessonVideo(models.Model):
    title=models.CharField(max_length=50)
    video_url = models.URLField(blank=True, null=True)
    
