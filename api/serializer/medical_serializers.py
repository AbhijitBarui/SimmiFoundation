from rest_framework import serializers
from fundraisers.models import *

# SERIALIZERS FOR MEDICAL API STARTS
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

# SERIALIZERS FOR MEDICAL API ENDS