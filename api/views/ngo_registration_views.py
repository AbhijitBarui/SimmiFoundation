from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from api.serializer.ngo_registration_serializers import ngo_registrationSerializer
from fundraisers.models.ngo_registration import ngo_registration


class getOnengo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,organisation_name, format=None):
        ngo = ngo_registration.objects.get(organisation_name=organisation_name)
        serializer = ngo_registrationSerializer(ngo, many=False)
        return Response({'status' : 200 ,  'message' : 'this is that one ngo','payload' : serializer.data})


class ngo_registrationAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        ngo_objs = ngo_registration.objects.all()
        Serializer = ngo_registrationSerializer(ngo_objs , many=True)
        return Response({'status' : 200 ,  'message' : 'here are the total ngos','payload' : Serializer.data})

class ngo_registrationAPIcreate(APIView):
    def post(self, request, format=None):
        serializer = ngo_registrationSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403 , 'errors' : serializer.errors , 'message' : 'something went wrong'})

        serializer.save()
        return Response({'status' : 200 , 'message' : 'your data is saved'})
    
class ngo_registrationAPIupdate(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, format=None):
        try:
            ngo_obj = ngo_registration.objects.get(organisation_name = request.data['organisation_name'])
            serializer = ngo_registrationSerializer(ngo_obj , data=request.data , partial = True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status' : 403 , 'errors' : serializer.errors , 'message' : 'something went wrong'})
            serializer.save()
            return Response({'status' : 200 , 'message' : 'your data is updated'})
        except Exception as e:
            print(e)
            return Response({'status' : 403 , 'message' : 'invalid organisation_name'})

class ngo_registrationAPIdelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, format=None):
        try:
            ngo_obj = ngo_registration.objects.get(organisation_name = request.data['organisation_name'])
            ngo_obj.delete()
            return Response({'status' : 200 , 'message' : 'your data is deleted'})
        except Exception as e:
            print(e)
            return Response({'status' : 403 , 'message' : 'invalid organisation_name'})



