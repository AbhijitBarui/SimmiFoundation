from rest_framework.views import APIView   #FOR CLASS BASE VIEW
from rest_framework.permissions import IsAuthenticated     # FOR  AUTHORIZATION
from rest_framework.response import Response


class getRoutes(APIView):
    def get(self,request):
        routes=[
        {'POST': 'api/token'},  # TOKEN
        {'POST': 'api/refresh_token'},  # REFRESH TOEKN

        {'POST': '/api/register'},
        {'POST': '/api/login'},
        {'POST': '/api/changepassword'},
        {'GET': 'api/carousel'},             #ALL API
        {'GET':'api/fundraiser_alldata'},    #FUNDRAISER
        {'GET':'api/event_data'},            # EVENT CURRENT AND INCOMING
        {'GET':'api/incoming_event_data'},
        {'GET':'api/what_p_say_alldata'},    # WHAT PEOPLE SAY 
        {'GET':'api/our_succ_story'},        #OUR SUCCESS STORY 
        {'GET':'api/our_volunteers'},        # OUR VOLUNTEERS 
        {'GET':'api/our_partners'},          # OUR PARTNERS

        {'GET': '/api/medical_fundraiser'},
        {'GET': '/api/medical_fundraiser/email'},
        {'POST': '/api/medical_fundraiser/create'},
        {'PATCH': '/api/medical_fundraiser/update'},

        {'GET': '/api/fundraiser_others'},
        {'GET': '/api/fundraiser_others/email_id'},
        {'POST': '/api/fundraiser_others/create'},
        {'PATCH': '/api/fundraiser_others/update'},
        {'DELETE': '/api/fundraiser_others/delete'},

        {'GET': '/api/campaigns/'},
        {'GET': '/api/campaigns/title'},
        {'POST': '/api/campaigns/create/'},
        {'PATCH': '/api/campaigns/update/'},
        {'DELETE': '/api/campaigns/delete/'},






        ]
        return Response(routes)