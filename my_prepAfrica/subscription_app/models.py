from django.db import models
from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication_app.models import CustomUser

class SubscribedUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,blank=True,null=True)
    is_subscribed = models.BooleanField(default=False)
    subscription_type = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    billing_info = models.TextField(blank=True, null=True)
    # Add any other subscription-related fields you may need

    