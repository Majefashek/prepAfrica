from django.urls import path
from .views import UpdateProgressView

urlpatterns = [
   path('update_progress/', UpdateProgressView.as_view(),name="update_progress"),
]
