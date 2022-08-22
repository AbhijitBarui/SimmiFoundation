from rest_framework.views import APIView  # FOR CLASS BASE VIEW
from rest_framework.permissions import IsAuthenticated  # FOR  AUTHORIZATION
from rest_framework.response import Response


class getRoutes(APIView):
    def get(self, request):
        routes = [
            {'POST': '/api/token'},
            {'POST': '/api/refresh_token'},

            {'POST': '/api/register'},
            {'POST': '/api/login'},
            {'POST': '/api/changepassword'},
            {'GET': '/api/loggeduser/id'},

            {'GET': '/api/carousel'},
            {'GET': '/api/fundraiser_alldata'},
            {'GET': '/api/event_data'},
            {'GET': '/api/incoming_event_data'},
            {'GET': '/api/what_p_say_alldata'},
            {'GET': '/api/our_succ_story'},
            {'GET': '/api/our_volunteers'},
            {'GET': '/api/our_partners'},

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

            # RAZORPAY APIs
            {'POST': '/api/razorpay_order'},
            {'POST': '/api/razorpay_callback'},

        ]
        return Response(routes)
