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




class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('DashBoard')  
        else:
            return render(request, self.template_name, {'error_message': 'Invalid email or password'})


class SignUpView(View):
    template_name = 'auth/signup.html'
    success_url = 'DashBoard'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        existing_user = CustomUser.objects.filter(email=email).exists()

        if existing_user:
            # User with the same email already exists, handle the error accordingly
            return render(request, self.template_name, {'error': 'User with this email already exists'})

        CustomUser.objects.create_user(email=email, password=password)

        return redirect(self.success_url)

class CustomPasswordResetView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        
        print(email)
        # Replace 'email' with the actual name of the email input field in your HTML form
        user = CustomUser.objects.get(email=email)
        user_pk= CustomUser.objects.get(email=email)
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
            return redirect('email_sent')
        except Exception:
            print(Exception)

    def get(self,request):
        template_name='auth/custom_password_reset.html'
        return render(request, template_name)
    

class PasswordChangeDone(View):
    template_name = 'auth/password_confirm.html'

    def validate_user_token(self, uidb64, token):
        try:
            email_bytes =base64.urlsafe_b64decode(uidb64)
            email = email_bytes.decode('utf-8')

            you='abdullahishuaibumaje@gmail.com'
            user = CustomUser.objects.get(email=email)
            if default_token_generator.check_token(user, token):
                return user
            
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
           pass
        return None

    def get(self, request, uidb64, token):
        user = self.validate_user_token(uidb64, token)
        if user is not None:
            context = {'valid_link': user is not None, 'uidb64': uidb64, 'token': token,'user':user}
            return render(request, self.template_name, context)
        else:
            context={'user':user,'uidb64':uidb64,'token':token}
            return render(request,self.template_name,context)

    def post(self, request, uidb64, token):
        uidb64 = request.POST.get('uidb64')
        token = request.POST.get('token')
        user = self.validate_user_token(uidb64, token)
        if user is not None:
            password = request.POST.get('password')
            
            # Update the user's password
            user.set_password(password)
            user.save()

            # Password successfully changed. You can add any additional logic or redirect as needed.
            return redirect('DashBoard')  # Replace with your desired URL

        context = {'valid_link': False, 'uidb64': uidb64, 'token': token, 'invalid_password': True}
        return render(request, self.template_name, context)
    

class EmailSentView(TemplateView):
    template_name = "auth/email_sent.html"