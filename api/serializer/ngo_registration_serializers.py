from rest_framework import serializers
from fundraisers.models.ngo_registration import ngo_registration

#SERIALIZERS FOR NGO_REGISTRATION PAGE STARTS

class ngo_registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ngo_registration
        fields = '__all__'


#SERIALIZERS FOR NGO_REGISTRATION PAGE ENDS