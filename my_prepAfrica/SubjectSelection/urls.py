from django.contrib import admin
from django.urls import path, include
from .views import ViewSubjects,ViewUnits,ViewLessons, SearchView

urlpatterns = [
    path('subjects/', ViewSubjects.as_view(), name="manage_subjects"),
    #path('subjects/add/', AddSubject.as_view(), name="add_subject"),
    #path('subjects/remove/<int:subject_id>/', RemoveSubject.as_view(), name="remove_subject"),
    path('ViewUnits/<int:subject_id>/', ViewUnits.as_view(), name="view_units"),
    path('units/view_lessons/<int:unit_id>/', ViewLessons.as_view(), name="view_lessons"),
    path('SearchSubjects/<str:query>/', SearchView.as_view()),
]