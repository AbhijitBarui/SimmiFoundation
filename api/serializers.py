
from rest_framework import serializers

from home_app.models import *


#serialize the model  CAROUSEL
class carouselSerializer(serializers.ModelSerializer):
    class Meta:
        model=carousel
        fields= '__all__'



#serialize the model  TRENDING_FUNDRAISER
class trending_fundraisersSerializer(serializers.ModelSerializer):
    class Meta:
        model=trending_fundraisers
        fields= '__all__'



#serialize the model  INCOMING AND CURRENT EVENTS
class current_incoming_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=current_incoming_event
        fields= '__all__'


#serialize the model  WHAT PEOPLE SAY
class what_people_saySerializer(serializers.ModelSerializer):
    class Meta:
        model=what_people_say
        fields= '__all__'


#serialize the model  OUR SUCCESS STORY 
class our_success_storySerializer(serializers.ModelSerializer):
    class Meta:
        model=our_success_story
        fields= '__all__'

#serialize the model  OUR VOLUNTEERS 
class our_volunteersSerializer(serializers.ModelSerializer):
    class Meta:
        model=our_volunteers
        fields= '__all__'


#serialize the model  OUR PARTNERS 
class our_partnersSerializer(serializers.ModelSerializer):
    class Meta:
        model=our_partners
        fields= '__all__'