from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from api.serializers import newuserregisterSerializer,newuserloginrSerializer
from api.serializers import *
from User_Auth.model import new_user
#from rest_framework import status
from django.contrib.auth.password_validation import validate_password












class newuserRegistrationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        password=request.data['password']
        length_pass=len(password)
        
        cpassword=request.data['cpassword']
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

        
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            token = get_tokens_for_user(data)
            return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)





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
    
        if (email==email_database and flag==True ):
            request.session['name']=user.name
            request.session['email']=user.email
            request.session['phone']=user.Phone
            # print(request.session['name'])
            # print(request.session['email'])
            # print(request.session['phone'])

            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


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

    check=check_password(oldpass,user.password)   #match old  and new password
    
   
    encryptpass=make_password(newpass)  #PASSWORD ENCRYPT
    print(encryptpass)
    request.data._mutable = True       # FOR  CHANGE IN SERIALIZE DATA
    request.data.update({'password':encryptpass })  #CHANGE THA DATA IN SERIALIZE DATA
    
    serializer.is_valid(raise_exception=True)
    
    if (check==True and passmatch):
            print(user.password)
            user.password=encryptpass
            user.save()
            return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

    else:
        return Response({'msg':'Password not match OR Incorrect old password'}, status=status.HTTP_200_OK)