
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core_app.urls')),
    path('api/auth/v1/', include('authentication_app.urls')),
    path('api/subjects/v1/',include('SubjectSelection.urls')),
    path('api/tests/v1/',include('Tests.urls')),
]
