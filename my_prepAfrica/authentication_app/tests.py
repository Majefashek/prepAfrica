from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser  # Import your CustomUser model
from .serializers import CustomTokenObtainPairSerializer  # Import your CustomUserSerializer
from .views  import MyTokenObtainPairView
from rest_framework_simplejwt.exceptions import AuthenticationFailed
import json


# Tests that token is obtained successfully with valid email and password
class MyTokenObtainPairViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('token_obtain_pair')

    def test_token_obtained_successfully(self):
        # Arrange
        email = 'test@example.com'
        password = 'testpassword'
        user = CustomUser.objects.create_user(email=email, password=password)
        data = {'email': email, 'password': password}
        #request = mocker.Mock(data=data)
        #view = MyTokenObtainPairView.as_view()
        #act
        response =  self.client.post(self.signup_url, data=data, format='json')

        # Assert
        assert response.status_code == 200
        assert 'access' in response.data
        assert 'refresh' in response.data

    # Tests that password is validated successfully with valid email and password
       # Tests that password is validated successfully with valid email and password
    def test_password_valid_credentials(self):
        # Arrange
        email = 'test@example.com'
        password =  "testpassword"
        user = CustomUser.objects.create_user(email=email, password=password)
        data = {'email': email, 'password': password}
        serializer = CustomTokenObtainPairSerializer(data=data)
        serializer.is_valid(raise_exception=True)

    def test_invalid_email(self):
        data = {
            "email": "invalid@example.com",
            "password": "testpassword"
        }
        serializer = CustomTokenObtainPairSerializer(data=data)
        with self.assertRaises(AuthenticationFailed) as context:
            serializer.is_valid(raise_exception=True)
        
        exception_message = str(context.exception.args[0])  # Extract the exception details
        #error_message = exception_dict.get("string", "")  # Extract the error message

        self.assertEqual(
            exception_message,
            "Invalid Email"
        )


    
            
    
        