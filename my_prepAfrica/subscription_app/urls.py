from django.urls import path
from .views import MakePayment, VerifyPaymentAndSubscribe,VerifyUSerSubscribed

urlpatterns = [
    path('make_payment/',MakePayment.as_view(), name='make_payment'),
    path('verify/<str:reference>/',VerifyPaymentAndSubscribe.as_view(), name='Verify_and_subscribe'),
    path('verifysubscription/',VerifyUSerSubscribed.as_view(), name='Verifysubscription')
    # Add other URLs as needed
]
