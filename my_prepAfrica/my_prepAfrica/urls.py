
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_app.urls')),
    path('auth/', include('authentication_app.urls')),
    path('subjects/',include('SubjectSelection.urls')),
    path('tests/',include('Tests.urls')),
]
