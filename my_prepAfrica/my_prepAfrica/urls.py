
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core_app.urls')),
    path('api/v1/', include('authentication_app.urls')),
    path('api/v1/subjects/',include('SubjectSelection.urls')),
    path('api/v1/tests/',include('Tests.urls')),
    path('api/v1/',include('subscription_app.urls')),
    path('api/v1/', include('ProgressTrackkingApp.urls')),
]
