from rest_framework import serializers
from fundraisers.models.fundraisers_medical import Fundraisers_medical


class FundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraisers_medical
        fields = '__all__'


class CreateMedicalFundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraisers_medical
        fields = '__all__'


class UpdateMedicalFundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraisers_medical
        fields = '__all__'
