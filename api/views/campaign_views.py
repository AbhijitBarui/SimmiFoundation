from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from api.serializer.cmapaign_serializers import campaign_Serializer
from fundraisers.models.campaign import Campaign

class getCampaign(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        campaigns = Campaign.objects.all()
        serializer = campaign_Serializer(campaigns, many=True)
        return Response(serializer.data)


class getOneCampaign(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, title, format=None):
        campaigns = Campaign.objects.get(title=title)
        serializer = campaign_Serializer(campaigns, many=False)
        return Response(serializer.data)


class CreateCampaign(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = campaign_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            Campaign = serializer.save()
            return Response({'msg':'Campaign Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCampaign(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, format=None):
        try:
            obj = Campaign.objects.get(title=request.data['title'])
            serializer = campaign_Serializer(obj, data=request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
            serializer.save()
            return Response({'status': 200, 'message': 'Campaign is updated'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'invalid title'})

class DeleteCamapign(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, format=None):
        try:
            fundraiser_others_obj = Campaign.objects.get(title = request.data['title'])
            fundraiser_others_obj.delete()
            return Response({'status' : 200 , 'message' : 'Campaign is deleted'})
        except Exception as e:
            print(e)
            return Response({'status' : 403 , 'message' : 'invalid title'})