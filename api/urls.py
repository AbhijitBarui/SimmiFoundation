from django.urls import path
from .views.routes import getRoutes
from .views.homepage import *
from .views.medical_fundraiser_views import getMedicalFundraiser, getOneMedicalFundraiser, CreateMedicalFundraiser, UpdateMedicalFundraiser
from .views.fundraisers_others_views import getOneothersfundraiser, fundraiser_othersAPI, fundraiser_othersAPIcreate, fundraiser_othersAPIdelete, fundraiser_othersAPIupdate
from .views.user_auth_view import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns=[
    path('',getRoutes.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # GENERATE TOKEN
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),  # GENERATE REFRESH TOKE

    path('medical_fundraiser/', getMedicalFundraiser.as_view()),
    path('medical_fundraiser/<str:email>', getOneMedicalFundraiser.as_view()),
    path('medical_fundraiser/create/', CreateMedicalFundraiser.as_view(), name='create_medical_fundraiser'),
    path('medical_fundraiser/update/', UpdateMedicalFundraiser.as_view(), name='update_medical_fundraiser'),

    path('carousel/',getCarousel.as_view()),                                  #CAROUSEL API
    path('fundraiser_alldata/',  getFundraiser_data.as_view(), name ='fundraiser_data'),   # FUNDRAISER ALL DATA API
    path('event_data/',getEvent.as_view()),                                       #ALL CURRENT AND INCOMING EVENT DATA  API
    path('incoming_event_data/',getincoming_Event.as_view()),
    path('what_p_say_alldata/',getWhat_people_say.as_view()),                                  # WHAT PEOPLE SAY API
    path('our_succ_story/',getOur_success_story.as_view()),                       #OUR SUCCESS STORY
    path('our_volunteers/',getOur_volunteer.as_view()),                          #OUR VOLUNTEERS
    path('our_partners/',getOur_partner.as_view()),                           #OUR PARTNERS

    path('fundraiser_others/', fundraiser_othersAPI.as_view()),
    path('fundraiser_others/<str:email_id>', getOneothersfundraiser.as_view()),
    path('fundraiser_others/create/', fundraiser_othersAPIcreate.as_view(), name='create_fundraiser_others'),
    path('fundraiser_others/update/', fundraiser_othersAPIupdate.as_view(), name='update_fundraiser_others'),
    path('fundraiser_others/delete/', fundraiser_othersAPIdelete.as_view(), name='delete_fundraiser_others'),



    ### USER AUTH
    path('register/',newuserRegistrationView.as_view()),
    path('login/',newuserLoginView.as_view()),
    path('changepassword/',UserChangePasswordView.as_view()),
]
