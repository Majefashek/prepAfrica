from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from rest_framework import serializers




CustomUser =get_user_model()
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        print(email)
        password = attrs.get("password")

        if email and password:
            try:
                user = CustomUser.objects.get(email=email)
            except:
                raise AuthenticationFailed("Invalid Email")

            if  not user.check_password(password):
                print(password)
                raise AuthenticationFailed("No active account found with the given password")
        else:
            raise AuthenticationFailed("Both email and password are required.")

        return super().validate(attrs)
