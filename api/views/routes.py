from rest_framework.views import APIView   #FOR CLASS BASE VIEW
from rest_framework.permissions import IsAuthenticated     # FOR  AUTHORIZATION
from rest_framework.response import Response


class getRoutes(APIView):
    def get(self,request):
        routes=[
        {'GET': 'api/carousel'},             #ALL API
        {'GET':'api/fundraiser_alldata'},    #FUNDRAISER
        {'GET':'api/event_data'},            # EVENT CURRENT AND INCOMING
        {'GET':'api/what_p_say_alldata'},    # WHAT PEOPLE SAY 
        {'GET':'api/our_succ_story'},        #OUR SUCCESS STORY 
        {'GET':'api/our_volunteers'},        # OUR VOLUNTEERS 
        {'GET':'api/our_partners'},        # OUR PARTNERS

        {'GET': '/api/medical_fundraiser'},
        {'GET': '/api/medical_fundraiser/email'},
        {'POST': '/api/medical_fundraiser/create'},
        {'PATCH': '/api/medical_fundraiser/update'},

        {'POST': 'api/token'},        #TOKEN
        {'POST': 'api/refresh_token'}, #  REFRESH TOEKN

        ]
        return Response(routes)