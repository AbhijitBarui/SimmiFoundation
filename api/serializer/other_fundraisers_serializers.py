from rest_framework import serializers
from fundraisers.models.fundraisers_others import *

# SERIALIZERS FOR FUNDRAISERS_OTHERS PAGE STARTS


class fundraiser_othersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraiser_others
        fields = '__all__'


# SERIALIZERS FOR FUNDRAISERS_OTHERS PAGE ENDS