from django.urls import path
from .views import TestEvaluationView,MyTestView

urlpatterns = [
    path('test/<int:test_id>/evaluate/', TestEvaluationView.as_view(), name='evaluate_test'),
    path('mytest',MyTestView.as_view(),name="mytest")
    #path('test/', TestEvaluationView.as_view(), name='evaluate_test'),
]
