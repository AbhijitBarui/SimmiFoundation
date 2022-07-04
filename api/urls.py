from django.urls import path

from .views.medical_fundraiser_views import getMedicalFundraiser, getOneMedicalFundraiser, CreateMedicalFundraiser, UpdateMedicalFundraiser
from .views.routes import getRoutes
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', getRoutes.as_view()),
    path('medical_fundraiser/', getMedicalFundraiser.as_view()),
    path('medical_fundraiser/<str:email>', getOneMedicalFundraiser.as_view()),
    path('medical_fundraiser/create/', CreateMedicalFundraiser.as_view(), name='create_medical_fundraiser'),
    path('medical_fundraiser/update/', UpdateMedicalFundraiser.as_view(), name='update_medical_fundraiser'),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
