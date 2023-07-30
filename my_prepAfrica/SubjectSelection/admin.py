from django.contrib import admin
from .models import Subjects,Enrollment,Lesson,Unit,LessonVideo,MyLessonVideo

admin.site.register(Subjects)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Unit)
admin.site.register(LessonVideo)
admin.site.register(MyLessonVideo)
