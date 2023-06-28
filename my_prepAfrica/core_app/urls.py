from .views import DashBoardView
from django.urls import path

urlpatterns = [
    path('', DashBoardView.as_view(), name='DashBoard'),
]
