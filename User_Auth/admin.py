from django.contrib import admin
from User_Auth.models.new_user import newuser
from User_Auth.models.custom_user_model import User, UserNotificationSetting, AlternateUserEmail
from User_Auth.models import *

# Register your models here.
admin.site.register(newuser) 
admin.site.register(User) 
admin.site.register(UserNotificationSetting) 
admin.site.register(AlternateUserEmail) 
