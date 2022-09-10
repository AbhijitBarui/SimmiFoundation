from django.urls import path
from .views.routes import getRoutes
from .views.homepage import *
from .views.medical_fundraiser_views import getMedicalFundraiser, getOneMedicalFundraiser, CreateMedicalFundraiser, UpdateMedicalFundraiser
from .views.fundraisers_others_views import getOneothersfundraiser, fundraiser_othersAPI, fundraiser_othersAPIcreate, fundraiser_othersAPIdelete, fundraiser_othersAPIupdate
from .views.campaign_views import getCampaign, getOneCampaign, CreateCampaign, UpdateCampaign, DeleteCamapign
from .views.user_auth_view import *
from .views.faq_views import *
from .views.ngo_registration_views import getOnengo,ngo_registrationAPI,ngo_registrationAPIcreate,ngo_registrationAPIupdate,ngo_registrationAPIdelete

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views.payment import CallbackView, PaymentView


urlpatterns=[
    path('',getRoutes.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # GENERATE TOKEN
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),  # GENERATE REFRESH TOKE

    path('medical_fundraiser/', getMedicalFundraiser.as_view()),
    path('medical_fundraiser/<str:email>', getOneMedicalFundraiser.as_view()),
    path('medical_fundraiser/create/', CreateMedicalFundraiser.as_view(), name='create_medical_fundraiser'),
    path('medical_fundraiser/update/', UpdateMedicalFundraiser.as_view(), name='update_medical_fundraiser'),

    path('carousel/',getCarousel.as_view()),                                
    path('fundraiser_alldata/',  getFundraiser_data.as_view(), name ='fundraiser_data'),   
    path('event_data/',getEvent.as_view()),                                       
    path('incoming_event_data/',getincoming_Event.as_view()),
    path('what_p_say_alldata/',getWhat_people_say.as_view()),                                  
    path('our_succ_story/',getOur_success_story.as_view()),                       
    path('our_volunteers/',getOur_volunteer.as_view()),                          
    path('our_partners/',getOur_partner.as_view()),

    path('ngo_registration/', ngo_registrationAPI.as_view()),
    path('ngo_registration/<str:organisation_name>', getOnengo.as_view()),
    path('ngo_registration/create/', ngo_registrationAPIcreate.as_view(), name='create_fundraiser_others'),
    path('ngo_registration/update/', ngo_registrationAPIupdate.as_view(), name='update_fundraiser_others'),
    path('ngo_registration/delete/', ngo_registrationAPIdelete.as_view(), name='delete_fundraiser_others'),

    path('fundraiser_others/', fundraiser_othersAPI.as_view()),
    path('fundraiser_others/<str:email_id>', getOneothersfundraiser.as_view()),
    path('fundraiser_others/create/', fundraiser_othersAPIcreate.as_view(), name='create_fundraiser_others'),
    path('fundraiser_others/update/', fundraiser_othersAPIupdate.as_view(), name='update_fundraiser_others'),
    path('fundraiser_others/delete/', fundraiser_othersAPIdelete.as_view(), name='delete_fundraiser_others'),

    path('campaigns/', getCampaign.as_view()),
    path('campaigns/<str:title>', getOneCampaign.as_view()),
    path('campaigns/create/', CreateCampaign.as_view()),
    path('campaigns/update/', UpdateCampaign.as_view()),
    path('campaigns/delete/', DeleteCamapign.as_view()),


    # USER AUTH
    path('register/',newuserRegistrationView.as_view()),
    path('login/',newuserLoginView.as_view()),
    path('changepassword/',UserChangePasswordView.as_view()),
    path('loggeduser/<int:id>', getOneUserByid.as_view()),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view()),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
  
    path('razorpay_order', PaymentView.as_view(), name='razorpay_order'),
    path('razorpay_callback', CallbackView.as_view(), name='razorpay_callback'),

    # FAQ
    path('faq/create/', faq_APIcreate.as_view()),
    path('faq/<str:username>', getfaq.as_view()),
]
