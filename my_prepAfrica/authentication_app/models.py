from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission  # Import additional models
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def __init__(self, model=None):
        super().__init__()
        self.model = model
    
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user =self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    username=models.CharField(blank=True,max_length=300)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # For now, return True as a placeholder for user permissions.
        return True

    def has_module_perms(self, app_label):
        # For now, return True as a placeholder for module permissions.
        return True
