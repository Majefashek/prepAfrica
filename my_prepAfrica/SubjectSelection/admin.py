from django.contrib import admin
from .models import Subjects,Enrollment,Lesson,Unit

admin.site.register(Subjects)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Unit)
