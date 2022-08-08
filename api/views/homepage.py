from rest_framework.views import APIView  # FOR CLASS BASE VIEW
from rest_framework.permissions import IsAuthenticated  # FOR  AUTHORIZATION
from rest_framework.response import Response
from api.serializer.homepage_serializers import *


class getCarousel(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("USER :", request.user)
        projects = carousel.objects.all()
        serializer = carouselSerializer(projects, many=True)
        return Response(serializer.data)


class getEvent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Current_incoming_event.objects.all()
        serializer = current_incoming_eventSerializer(projects, many=True)
        return Response(serializer.data)


class getincoming_Event(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Incoming_event.objects.all()
        serializer =incoming_eventSerializer(projects, many=True)
        return Response(serializer.data)




# FUNDRAISER_ALL DATA  API VIEW
# fetch the all data of trending_fundraisers model
class getFundraiser_data(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("USER :", request.user)
        projects = Trending_fundraisers.objects.all()
        serializer = trending_fundraisersSerializer(projects, many=True)
        return Response(serializer.data)


# FUNDRAISER_ALL DATA  API VIEW
# fetch the all data of trending_fundraisers model
class getOur_partner(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("USER :", request.user)
        projects = Our_partners.objects.all()
        serializer = our_partnersSerializer(projects, many=True)
        return Response(serializer.data)


# FUNDRAISER_ALL DATA  API VIEW
# fetch the all data of trending_fundraisers model
class getOur_success_story(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("USER :", request.user)
        projects = Our_success_story.objects.all()
        serializer = our_success_storySerializer(projects, many=True)
        return Response(serializer.data)


# FUNDRAISER_ALL DATA  API VIEW
# fetch the all data of trending_fundraisers model
class getOur_volunteer(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("USER :", request.user)
        projects = Our_volunteers.objects.all()
        serializer = our_volunteersSerializer(projects, many=True)
        return Response(serializer.data)


# FUNDRAISER_ALL DATA  API VIEW
# fetch the all data of trending_fundraisers model
class getWhat_people_say(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("USER :", request.user)
        projects = What_people_say.objects.all()
        serializer = what_people_saySerializer(projects, many=True)
        return Response(serializer.data)