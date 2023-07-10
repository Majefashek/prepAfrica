from django.contrib import admin
from django.urls import path, include
from .views import ManageSubjects,AddSubject,RemoveSubject,ViewUnits,ViewLessons 

urlpatterns = [
    path('subjects/', ManageSubjects.as_view(), name="manage_subjects"),
    path('subjects/add/', AddSubject.as_view(), name="add_subject"),
    path('subjects/remove/<int:subject_id>/', RemoveSubject.as_view(), name="remove_subject"),
    path('subjects/view_units/<int:subject_id>/', ViewUnits.as_view(), name="view_units"),
    path('units/view_lessons/<int:unit_id>/', ViewLessons.as_view(), name="view_lessons"),
]