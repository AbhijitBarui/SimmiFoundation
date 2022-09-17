from rest_framework import serializers
from User_Auth.models import *







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


#========================= Custom User Model Serializers ==================================#
from User_Auth import google
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from decouple import config
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=50,min_length=8,write_only=True
    )
    cpassword = serializers.CharField(
        max_length=50,min_length=8,write_only=True
    )

    class Meta:
        model = User
        fields = ['id','email','password', "phone_number", "cpassword", "first_name"]

    def validate(self,attrs):
        email = attrs.get('email',None)
        if email is None:
            raise serializers.ValidationError(
                'User Should Have email address'
            )
        
        elif attrs.get("password") != attrs.get("cpassword"):
            raise serializers.ValidationError(
                'Password and Confirm password doesn\'t match'
            )
        
        return attrs
    
    def create(self, validated_data):
        del validated_data['cpassword']
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "is_superuser", "is_verified", "is_active", "is_staff", "groups", "user_permissions"]

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotificationSetting
        fields = "__all__"
        
class AlternateUserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlternateUserEmail
        fields = "__all__"

class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=50,min_length=8,write_only=True
    )
    cpassword = serializers.CharField(
        max_length=50,min_length=8,write_only=True
    )
    oldpassword = serializers.CharField(
        max_length=50,min_length=8,write_only=True
    )

    def validate(self, attrs):
        old_pass = attrs.get('oldpassword')
        new_pass = attrs.get('password')
        confirm_pass = attrs.get('cpassword')
        request = self.context.get('request')
        if new_pass != confirm_pass:
            raise serializers.ValidationError("New Password Doesn't Match with Confirm Password")
        
        if not request.user.check_password(old_pass):
            raise serializers.ValidationError("Password Doesn't Match")
        
        request.user.set_password(new_pass)
        request.user.save()
        return attrs

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['id'] = user.id
        token['email'] = user.email

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['id'] = self.user.id
        data["email"] = self.user.email
        return data

class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        print(user_data)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        if user_data['aud'] != config('GOOGLE_CLIENT_ID'):

            raise AuthenticationFailed('oops, who are you?')
        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(provider, user_id, email, name)

def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:

            registered_user = authenticate(
                email=email, password=config('SOCIAL_SECRET'))

            return {
                'id': registered_user.id,
                'email': registered_user.email,
                'tokens': registered_user.tokens()}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'email': email,
            'password': config('SOCIAL_SECRET'),
            'first_name': name
            }
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=config('SOCIAL_SECRET'))
        return {
            'email': new_user.email,
            'id': new_user.id,
            'tokens': new_user.tokens()
        }