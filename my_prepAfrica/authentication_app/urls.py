
from django.urls import path, include
from . views import SignUpView,CustomPasswordResetView,PasswordChangeDone,EmailSentView,MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path("login/",LoginView.as_view(),name="login"),
    path("signup/",SignUpView.as_view(),name="signup"),
    path("password_reset/",CustomPasswordResetView.as_view(), name="password_reset"),
    path("password_change_done/<str:uidb64>/<str:token>/", PasswordChangeDone.as_view(), name="password_change_done"),#email form,
    path("email_sent/",EmailSentView.as_view(), name="email_sent"),
    #path("reset_password/",auth_views.PasswordResetView.as_view(),name="reset_password"),#email form
    #path("reset_password_done/",auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),#confirmation that email is submitted
    #path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),#link to confirm
    #path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),# succesfully changed
   
]
