from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

AUTH_PROVIDERS = {
    'google': 'google',
    'email': 'email'
}

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if email is None:
            raise ValueError("User Must Have Email")
        
        user = self.model(email = self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password=None):
        if password is None:
            raise ValueError("Password should not be None")
        user = self.create_user(email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255,unique=True)
    preferred_currency = models.CharField(max_length=30,blank=True)
    country = models.CharField(max_length=30,blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=255,blank=True)
    pincode = models.CharField(max_length=10,blank=True)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    auth_provider = models.CharField(max_length=30, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

class UserNotificationSetting(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="settings")
    monthly_updates = models.BooleanField(default=True)
    borrower_updates = models.BooleanField(default=True)
    repayment_emails = models.BooleanField(default=True)
    autolend_emails = models.BooleanField(default=True)
    update_to_alt_emails = models.BooleanField(default=False)

class AlternateUserEmail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="alt_emails")
    email = models.EmailField()
    send_update = models.BooleanField(default=False)