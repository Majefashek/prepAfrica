from django.contrib import admin
from django.urls import path, include
from .views import ViewSubjects,ViewUnits,ViewLessons, SearchView, EnrollSubject,GetEnrolledSubject

urlpatterns = [
    path('',ViewSubjects.as_view(), name="manage_subjects"),
    path('enroll/<int:subject_id>/', EnrollSubject.as_view(), name="add_subject"),
    path('getenrolled/', GetEnrolledSubject.as_view(), name="remove_subject"),
    path('ViewUnits/<int:subject_id>/', ViewUnits.as_view(), name="view_units"),
    path('units/view_lessons/<int:unit_id>/', ViewLessons.as_view(), name="view_lessons"),
    path('SearchSubjects/<str:query>/', SearchView.as_view()),
]