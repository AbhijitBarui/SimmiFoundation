from rest_framework import serializers
from home_app.models import *
from fundraisers.models.fundraisers_medical import Fundraisers_medical
from fundraisers.models.fundraisers_others import Fundraiser_others

##### FOR USER VALIDATIONS START #####
from urllib import request
from User_Auth.model import newuser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password,check_password
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import PasswordResetTokenGenerator
##### FOR USER VALIDATIONS END #####

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }






# SERIALIZERS FOR MEDICAL API STARTS
class FundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraisers_medical
        fields = '__all__'


class CreateMedicalFundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraisers_medical
        fields = '__all__'


class UpdateMedicalFundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraisers_medical
        fields = '__all__'

# SERIALIZERS FOR MEDICAL API ENDS





############ SERIALIZERS FOR HOME PAGE STARTS ######################
# the model  CAROUSEL
class carouselSerializer(serializers.ModelSerializer):
    class Meta:
        model=carousel
        fields= '__all__'



#serialize the model  TRENDING_FUNDRAISER
class trending_fundraisersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trending_fundraisers
        fields= '__all__'



#serialize the model  INCOMING AND CURRENT EVENTS
class current_incoming_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Current_incoming_event
        fields= '__all__'

class incoming_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Incoming_event
        fields= '__all__'

#serialize the model  WHAT PEOPLE SAY
class what_people_saySerializer(serializers.ModelSerializer):
    class Meta:
        model=What_people_say
        fields= '__all__'


#serialize the model  OUR SUCCESS STORY 
class our_success_storySerializer(serializers.ModelSerializer):
    class Meta:
        model=Our_success_story
        fields= '__all__'

#serialize the model  OUR VOLUNTEERS 
class our_volunteersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Our_volunteers
        fields= '__all__'


#serialize the model  OUR PARTNERS 
class our_partnersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Our_partners
        fields= '__all__'


############ SERIALIZERS FOR HOME PAGE END ######################




# SERIALIZERS FOR FUNDRAISERS_OTHERS PAGE STARTS


class fundraiser_othersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraiser_others
        fields = '__all__'


# SERIALIZERS FOR FUNDRAISERS_OTHERS PAGE ENDS




####### USER AUTAH SERIALIZE START  #############
class newuserregisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = newuser
        fields = '__all__' 


class newuserloginrSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  
  class Meta:
    model = newuser
    fields = ['email', 'password']


class UserChangePasswordSerializer(serializers.Serializer):
    oldpassword = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
#   cpassword = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        maodel=newuser
        fields = ['password', 'cpassword','email']


####### USER AUTAH SERIALIZE END  #############