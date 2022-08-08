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



class UserChangePasswordSerializer(serializers.Serializer):
    oldpassword = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
#   cpassword = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        maodel=newuser
        fields = ['password', 'cpassword','email']



class newuserrSerializer(serializers.ModelSerializer):
  class Meta:
    model = newuser
    fields = ['email', 'name','phone']










####### USER AUTAH SERIALIZE END  #############