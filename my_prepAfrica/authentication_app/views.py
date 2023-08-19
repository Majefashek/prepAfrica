from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CustomUser,CustomUserManager
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .forms import CustomPasswordChangeForm
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
import base64
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializers import CustomUserSerializer




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    pass


class SignUpView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        print(password)
        if email:
            if password:

                newuser, created = CustomUser.objects.get_or_create(email=email)
                newuser.set_password(password)
                newuser.save()
                return Response({'message':'Succesfully registered'})
            else:
                return Response({'Error':'Please Provide Password'})
        else:
                return Response({'Error':'Please Provide Password'})




        if not created:
            # User with the same email already exists, handle the error accordingly
            return Response({'error': 'User with this email already exists'})

        newuser_serialized = CustomUserSerializer(newuser)
        userdata = newuser_serialized.data
        return Response(userdata)


class CustomPasswordResetView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        
        print(email)
        # Replace 'email' with the actual name of the email input field in your HTML form
        try:
            user = CustomUser.objects.get(email=email)
        except:
            return Response({'Error':'User Does Not Exist'})
                # Generate the uidb64 value
        uidb64 = urlsafe_base64_encode(force_bytes(email))
        current_site = get_current_site(request)
        token = default_token_generator.make_token(user)
        confirmation_url = reverse('password_change_done', kwargs={'uidb64':uidb64 , 'token': token})
        # Replace 'uidb64' with the actual name of the parameter in your URL pattern
        
        activation_link = f'http://{current_site.domain}{confirmation_url}'
        email_subject = 'Activate Your Account'
        email_body = f'Please click the following link to activate your account: {activation_link}'

        email = EmailMessage(email_subject, email_body, to=[email])
        try:
            email.send()
            return Response({'success':'email_sent'})
        except Exception:
            e=Exception
            return Response({'error':'Email Not Sent'})

    

class PasswordChangeDone(APIView):

    def validate_user_token(self, uidb64, token):
        try:
            email_bytes =base64.urlsafe_b64decode(uidb64)
            email = email_bytes.decode('utf-8')

            you='abdullahishuaibumaje@gmail.com'
            user = CustomUser.objects.get(email=email)
            userserialized=CustomUserSerializer(user)
            myuser=userserialized.data
            if default_token_generator.check_token(user, token):
                return myuser
            
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
           pass
        return None

    def get(self, request, uidb64, token):
        user = self.validate_user_token(uidb64, token)
        if user is not None:
            context = {'valid_link': user is not None, 'uidb64': uidb64, 'token': token,'user':user}
            return Response(context)
        else:
            context={'user':user,'uidb64':uidb64,'token':token}
            return Response(context)

    def post(self, request, uidb64, token): 
        user_id = self.validate_user_token(uidb64, token)['id']
        user=CustomUser.objects.get(id=user_id)
        if user is not None:
            password = request.data.get('password')
            
            # Update the user's password
            user.set_password(password)
            user.save()

            # Password successfully changed. You can add any additional logic or redirect as needed.
            return Response('Success')  # Replace with your desired URL

        context = {'valid_link': False, 'uidb64': uidb64, 'token': token, 'invalid_password': True,'user':user}
        return Response(context)
    

class EmailSentView(TemplateView):
    template_name = "auth/email_sent.html"