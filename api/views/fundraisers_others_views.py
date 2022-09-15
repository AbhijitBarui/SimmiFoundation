from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from api.serializer.other_fundraisers_serializers import fundraiser_othersSerializer
from fundraisers.models.fundraisers_others import Fundraiser_others



class getOneothersfundraiser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,email_id, format=None):
        fundraisers = Fundraiser_others.objects.get(email_id=email_id)
        serializer = fundraiser_othersSerializer(fundraisers, many=False)
        return Response({'status' : 200 ,  'message' : 'here are the total campaigns','payload' : serializer.data})


class fundraiser_othersAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        fundraiser_others_objs = Fundraiser_others.objects.all()
        Serializer = fundraiser_othersSerializer(fundraiser_others_objs , many=True)
        return Response({'status' : 200 ,  'message' : 'here are the total campaigns','payload' : Serializer.data})

class fundraiser_othersAPIcreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = fundraiser_othersSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403 , 'errors' : serializer.errors , 'message' : 'something went wrong'})

        serializer.save()
        return Response({'status' : 200 , 'message' : 'your data is saved'})
    
class fundraiser_othersAPIupdate(APIView):

    permission_classes = [IsAuthenticated]
    def patch(self, request, format=None):
        try:
            fundraiser_others_obj = Fundraiser_others.objects.get(email_id = request.data['email_id'])
            serializer = fundraiser_othersSerializer(fundraiser_others_obj , data=request.data , partial = True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status' : 403 , 'errors' : serializer.errors , 'message' : 'something went wrong'})
            serializer.save()
            return Response({'status' : 200 , 'message' : 'your data is updated'})
        except Exception as e:
            print(e)
            return Response({'status' : 403 , 'message' : 'invalid email_id'})

class fundraiser_othersAPIdelete(APIView):

    permission_classes = [IsAuthenticated]
    def delete(self, request, format=None):
        try:
            fundraiser_others_obj = Fundraiser_others.objects.get(email_id = request.data['email_id'])
            fundraiser_others_obj.delete()
            return Response({'status' : 200 , 'message' : 'your data is deleted'})
        except Exception as e:
            print(e)
            return Response({'status' : 403 , 'message' : 'invalid email_id'})



