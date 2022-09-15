from rest_framework import serializers
from api.serializer.user_auth_serializers import *
from User_Auth.model import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout





from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.core.mail import send_mail
import os
import uuid




# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }








# REGISTRATION 
class newuserRegistrationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        password=request.data['password']
        length_pass=len(password)
        cpassword=request.data['Cpassword']
        email=request.data['email']

        #PASSWORD VALIDATION
        if(length_pass<6):
            raise serializers.ValidationError("Password must be greater than 6 character ")

        user=newuser.objects.filter(email=email)
        if(user):
            raise serializers.ValidationError("Already Exits Email ")
        if(password!=cpassword):
            raise serializers.ValidationError("Passwod not match")
        encryptpass=make_password(password)  #PASSWORD ENCRYPT
        print(encryptpass)
        request.data._mutable = True       # FOR  CHANGE IN SERIALIZE DATA
        request.data.update({'password':encryptpass })  #CHANGE THA DATA IN SERIALIZE DATA

        serializer = newuserregisterSerializer(data=request.data)
        print(serializer)

        
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            # print(data)
            token = get_tokens_for_user(data)
            return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)





# LOGIN
class newuserLoginView(APIView):
  permission_classes = [IsAuthenticated]
  #renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = newuserloginrSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        email=request.data['email']
        password=request.data['password']
        user=newuser.objects.get(email=email)
        print(user)
        email_database=user.email
        password_database=user.password
    
        flag=check_password(password,password_database)    #PASSWORD CHECK
        print(flag)
    
        if (email==email_database and flag==True ):    #flag==True
            request.session['name']=user.name
            request.session['email']=user.email
            request.session['phone']=user.phone
            # print(request.session['name'])
            # print(request.session['email'])
            # print(request.session['phone'])

            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success','id':user.id,'email':user.email}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


# CHANGE PASSWORD
class UserChangePasswordView(APIView):
  #renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data)
    email=request.data['email']
    newpass=request.data['password']
    cpass=request.data['cpassword']
    passmatch=(newpass==cpass)
    oldpass=request.data['oldpassword']
    
    user=newuser.objects.get(email=email)


    
    serializer.is_valid(raise_exception=True)
    
    if (newpass==cpass and passmatch):
            print(user.password)
            # user.password=encryptpass
            user.password=newpass           
            user.save()
            return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

    else:
        return Response({'msg':'Password not match OR Incorrect old password'}, status=status.HTTP_200_OK)




###################### GET USER BY ID FOR PROFILE #################
class getOneUserByid(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,id, format=None):
        user = newuser.objects.get(id=id)
        print(user)
        if (user):
            serializer = newuserrSerializer(user, many=False)
            return Response({'status' : 200 ,  'message' : 'user found', 'user is' :serializer.data})
        else:
            return Response({'msg':'User Not Fond Or Incorrect User Id'}, status=status.HTTP_200_OK)









################### SEND RESET PASSWORD EMAIL  ############################

class SendPasswordResetEmailView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email=request.data['email']
    if newuser.objects.filter(email=email):
        user = newuser.objects.get(email = email)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token1=str(uuid.uuid4())
        token = urlsafe_base64_encode(force_bytes(token1))
        link = 'http://localhost:3000/api/user/reset/'+uid+'/' +token  
        print('Encoded UID', uid)
        print('Token', token)
        print('Password Reset Link', link)

     
   
     


########################### MAIL SEND PROCESS ################3
        subject = "SIMMI FOUNDATION PASSWORD RESET  LINK  "  
        msg     = f'RESET PASSWORD LINK : {link}' 
        to      = user.email 
        mail_by    = os.environ.get('EMAIL_USER') 
        res     = send_mail(subject, msg,mail_by, [to])    
        if(res == 1):  
            msg = "Password RESET Mail Sent Successfuly"  
        else:  
            msg = "FAILED TO SEND MAIL"  
        return Response({msg})
    
    else:
        return Response({"msg":"Email Is Not Valid"})
 
########################### END MAIL SEND PROCESS ################

class UserPasswordResetView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        pass1=request.data['password']
        pass2=request.data['password2']
        if pass1 != pass2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")

        id = smart_str(urlsafe_base64_decode(uid))
        user = newuser.objects.get(id=id)

        encryptpass2=make_password((pass1))  #PASSWORD ENCRYPT
        print(encryptpass2)
        request.data._mutable = True       # FOR  CHANGE IN SERIALIZE DATA
        request.data.update({'pass1':encryptpass2 })  #CHANGE THA DATA IN SERIALIZE DATA
        user.password=encryptpass2

     
        user.save()
        return Response({'msg':'PASSWORD CHANGED SUCCESSFULLY'})
