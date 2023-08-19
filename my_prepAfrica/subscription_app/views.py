import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models  import SubscribedUser
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from django.http import JsonResponse, HttpResponseBadRequest
import json
from django.views.decorators.csrf import csrf_exempt
from .models import SubscribedUser



CustomUser=get_user_model()

class PayStackAPISubscriptionView(APIView):
        authentication_classes = [JWTAuthentication]  # Use JWT Authentication
        permission_classes = [IsAuthenticated]
        
        def post(self,request,**kwargs):
            plan=kwargs['plan']
            userEmail=request.user.email
            #!/bin/sh
            url="https://api.paystack.co/subscription"
            access_key="sk_test_4919e55cc28eefb19f14acfe1b7c351f65b51345"
            data={ 
              "customer":userEmail, 
              "plan": plan,
            }
            headers={
                "Authorization":f"Bearer {access_key}"
            }
            response=requests.post(url, headers=headers, json=data)
            return Response(response.json())



                            



    

class MakePayment(APIView):
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]
    def post(self, request):
        
        userEmail=request.user.email
        # send an api request to intialize transaction
        url = "https://api.paystack.co/transaction/initialize"
        secret_key = "sk_test_4919e55cc28eefb19f14acfe1b7c351f65b51345"
        headers = {
            "Authorization": f"Bearer sk_test_4919e55cc28eefb19f14acfe1b7c351f65b51345",
            "Content-Type": "application/json",
        }
        data = {
            "email":userEmail,
            "amount": "10000",
            "plan":"PLN_xdqn93oljibez0b"
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response_data = response.json()
            return JsonResponse(response_data)
        except requests.exceptions.RequestException as e:
            # Handle API request error
            return JsonResponse({"error": str(e)})

    

class VerifyPaymentAndSubscribe(APIView):
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]
    """This view verifies the payment and subscribes a user to our service."""
    def post(self, request,**kwargs):
        reference=kwargs['reference']
        print(reference)
        url="https://api.paystack.co/transaction/verify/"+reference+"/"
        secret_key = "sk_test_4919e55cc28eefb19f14acfe1b7c351f65b51345"
        val= f"Bearer {secret_key}",
        print(val)
        headers = {
            "Authorization": f"Bearer {secret_key}",
            
            "Content-Type": "application/json",
        }
        try:
            response = requests.get(url, headers=headers)
            print(response)
            response_data = response.json()
            if response_data.get('data', {}).get('status') == "success":
                user = request.user
                try:
                  GetSubscribedUser = SubscribedUser.objects.get(user=user)
                except SubscribedUser.DoesNotExist:
          
                  GetSubscribedUser = SubscribedUser.objects.create(user=user)
                GetSubscribedUser.is_subscribed = True  
                GetSubscribedUser.save()
                return Response({'message':'successfully subscribe'})
            else:
                return Response({'message':'Payment not verified'})
        except requests.exceptions.RequestException as e:
             #Handle API request error
            return Response({"error": str(e)})
class VerifyUSerSubscribed(APIView):
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user=request.user
        try:
          subUser=SubscribedUser.objects.get(user=user)
        except SubscribedUser.DoesNotExist:
            return Response({'message':'No'})
        
        if subUser.is_subscribed:
            return Response({'message':'Yes'})
        else:
            return Response({'message':'No'})

#class VerifyPaymentAndSubscribe(APIView):
 #   def process_successful_payment(self, data):
 #       user=SubscribedUser.objects.create(is_subscribed=True)
   #     user.save()

    #    data = json.loads(data)
      #  return Response(data)
        # Logic to handle successful payment event
     #   pass

   # def process_failed_payment(self, data):
        #return Response(data)
        # Logic to handle failed payment event
      #  pass

   # def process_dispute_created(self, data):
     #   return Response(data)
        # Logic to handle dispute created event
    #    pass

    #def post(self, request):
       # try:
         #   data = json.loads(request.body.decode('utf-8'))
       # except json.JSONDecodeError:
           # return HttpResponseBadRequest("Invalid JSON data")

        # Identify the event type
      #  event_type = data.get('event')
#
        # Route events based on their types
     ###   if event_type == 'charge.success':
           # self.process_successful_payment(data)  # Corrected: Add 'self.'
     #   elif event_type == 'charge.failed':
    #        self.process_failed_payment(data)  # Corrected: Add 'self.'
       # elif event_type == 'dispute.created':
         #   self.process_dispute_created(data)  # Corrected: Add 'self.'
        # Add more event handlers for other types of events

      #  return JsonResponse({'status': 'success'})


   
    # Add more functions for handling other event types as needed

    