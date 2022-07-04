from django.urls import path
from .views import *
from .views.routes import getRoutes
# from .views.carousel_view import getCarousel
# from .views.findraiser_data_view import getFundraiser_data
# from .views.events_view import getEvent
# from .views.what_people_say_view import getWhat_people_say
# from .views.our_success_story_view import getOur_success_story
# from .views.our_volunteers_view import getOur_volunteer
# from .views.our_partners_view import getOur_partner
from .views.homepage import *
#from api.views import Fundraiser_data_view
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns=[
    path('',getRoutes.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # GENERATE TOKEN
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),  # GENERATE REFRESH TOKE
    path('carousel/',getCarousel.as_view()),                                  #CAROUSEL API
    path('fundraiser_alldata/',  getFundraiser_data.as_view(), name ='fundraiser_data'),   # FUNDRAISER ALL DATA API
    path('event_data/',getEvent.as_view()),                                       #ALL CURRENT AND INCOMING EVENT DATA  API
    path('what_p_say_alldata/',getWhat_people_say.as_view()),                                  # WHAT PEOPLE SAY API
    path('our_succ_story/',getOur_success_story.as_view()),                       #OUR SUCCESS STORY
    path('our_volunteers/',getOur_volunteer.as_view()),                          #OUR VOLUNTEERS
    path('our_partners/',getOur_partner.as_view()),                           #OUR PARTNERS
    
]
