from django.urls import path
from .views import TestEvaluationView,MyTestView,ViewTestResult,Myoptions, MyQuestions

urlpatterns = [
    path('test/<int:test_id>/evaluate/', TestEvaluationView.as_view(), name='evaluate_test'),
    path('mytest',MyTestView.as_view(),name="mytest"),
    #path('test/', TestEvaluationView.as_view(), name='evaluate_test'),
    path('viewtest/<int:test_id>/',ViewTestResult.as_view(),name="viewtest"),
    path('questions/',MyQuestions.as_view(),name="questions"),

    path('options/',Myoptions.as_view(),name="options"),
]
