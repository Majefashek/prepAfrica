from django.urls import path
from .views import MakePayment, VerifyPaymentAndSubscribe,VerifyUSerSubscribed,PayStackAPISubscriptionView

urlpatterns = [
    path('make_payment/',MakePayment.as_view(), name='make_payment'),
    path('verify/<str:reference>/',VerifyPaymentAndSubscribe.as_view(), name='Verify_and_subscribe'),
    path('verifysubscription/',VerifyUSerSubscribed.as_view(), name='Verifysubscription'),
    path('paystackSubscription/<str:plan>/', PayStackAPISubscriptionView.as_view(), name='paystackAPISubscription'),
   
]
