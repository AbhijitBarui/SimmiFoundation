from rest_framework import serializers
from fundraisers.models.campaign import *


# SERIALIZER FOR CAMPAIGNS

class campaign_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
