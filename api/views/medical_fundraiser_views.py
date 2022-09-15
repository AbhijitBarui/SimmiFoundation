from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from api.serializer.medical_serializers import FundraiserSerializer, CreateMedicalFundraiserSerializer, UpdateMedicalFundraiserSerializer
from fundraisers.models.fundraisers_medical import Fundraisers_medical

class getMedicalFundraiser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        fundraisers = Fundraisers_medical.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)


class getOneMedicalFundraiser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,email, format=None):
        fundraisers = Fundraisers_medical.objects.get(email=email)
        serializer = FundraiserSerializer(fundraisers, many=False)
        return Response(serializer.data)


class CreateMedicalFundraiser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = CreateMedicalFundraiserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            Fundraisers_medical = serializer.save()
            return Response({'msg':'Medical Fundraiser Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateMedicalFundraiser(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, format=None):
        try:
            obj = Fundraisers_medical.objects.get(email=request.data['email'])
            serializer = UpdateMedicalFundraiserSerializer(obj, data=request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
            serializer.save()
            return Response({'status': 200, 'message': 'your data is updated'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'invalid email'})
