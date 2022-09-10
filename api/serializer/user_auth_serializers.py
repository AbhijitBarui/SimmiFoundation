from rest_framework import serializers
from User_Auth.model import *







####### USER AUTAH SERIALIZE START  #############

class newuserregisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    Cpassword=serializers.CharField(max_length=255,read_only=True)
    class Meta:
        model = newuser
        fields = ['email','name','password','Cpassword','phone'] 



class newuserloginrSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  
  class Meta:
    model = newuser
    fields = ['email', 'password']



class UserChangePasswordSerializer(serializers.ModelSerializer):
  oldpassword = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  cpassword = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  
  class Meta:
    model = newuser
    fields = ['email', 'password','cpassword','oldpassword']



class newuserrSerializer(serializers.ModelSerializer):
  class Meta:
    model = newuser
    fields = ['email', 'name','phone']


####### USER AUTAH SERIALIZE END  #############



########################## FORGOT PASSWORD RESET  EMAIL START ####################

class SendPasswordResetEmailSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    fields = ['email']



class UserPasswordResetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    uid = self.context.get('uid')
    token = self.context.get('token')
    return attrs

########################## FORGOT PASSWORD RESET  EMAIL END ####################
