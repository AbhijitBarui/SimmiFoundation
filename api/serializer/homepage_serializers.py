from rest_framework import serializers
from home_app.models import *


############ SERIALIZERS FOR HOME PAGE START  ######################

# the model  CAROUSEL
class carouselSerializer(serializers.ModelSerializer):
    class Meta:
        model=carousel
        fields= '__all__'



#serialize the model  TRENDING_FUNDRAISER
class trending_fundraisersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trending_fundraisers
        fields= '__all__'



#serialize the model  INCOMING AND CURRENT EVENTS
class current_incoming_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Current_incoming_event
        fields= '__all__'

class incoming_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Incoming_event
        fields= '__all__'

#serialize the model  WHAT PEOPLE SAY
class what_people_saySerializer(serializers.ModelSerializer):
    class Meta:
        model=What_people_say
        fields= '__all__'


#serialize the model  OUR SUCCESS STORY 
class our_success_storySerializer(serializers.ModelSerializer):
    class Meta:
        model=Our_success_story
        fields= '__all__'

#serialize the model  OUR VOLUNTEERS 
class our_volunteersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Our_volunteers
        fields= '__all__'


#serialize the model  OUR PARTNERS 
class our_partnersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Our_partners
        fields= '__all__'


############ SERIALIZERS FOR HOME PAGE END ######################
