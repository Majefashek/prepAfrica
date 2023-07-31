from django.urls import path
from .views import TestEvaluationView,MyTestView,ViewTestResult,Myoptions, MyQuestions,MyLessonTests,MySubjectTests,MyUnitTests

urlpatterns = [
    path('evaluate/<int:test_id>/', TestEvaluationView.as_view(), name='evaluate_test'),
    path('getSubjTest/<int:subject_id>/', MySubjectTests.as_view(), name='subject_tests'),
    path('mytest/', MyTestView.as_view(), name='mytest'),
    path('viewtest/<int:test_id>/', ViewTestResult.as_view(), name='viewtest'),
    path('questions/', MyQuestions.as_view(), name='questions'),
    #path('options/', MyOptions.as_view(), name='options'),
]
