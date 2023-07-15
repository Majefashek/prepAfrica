
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core_app.urls')),
    path('api/v1/auth/', include('authentication_app.urls')),
    path('api/v1/subjects/',include('SubjectSelection.urls')),
    path('api/v1/tests/',include('Tests.urls')),
]
