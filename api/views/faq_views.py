from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from api.serializer.faq_serializers import faq_Serializer
from faq.models import faq


class getfaq(APIView):
    def get(self, request,username, format=None):
        faq1 = faq.objects.get(username=username)
        serializer = faq_Serializer(faq1, many=False)
        return Response({'status' : 200 ,  'message' : 'this is faq of the user','payload' : serializer.data})



class faq_APIcreate(APIView):
    def post(self, request, format=None):
        serializer = faq_Serializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403 , 'errors' : serializer.errors , 'message' : 'something went wrong'})

        serializer.save()
        return Response({'status' : 200 , 'message' : 'your data is saved'})
    