from rest_framework import serializers
from faq.models import *

#SERIALIZERS FOR FAQ PAGE STARTS

class faq_Serializer(serializers.ModelSerializer):
    class Meta:
        model = faq
        fields = '__all__'

#SERIALIZERS FOR FAQ PAGE ENDS