from django.contrib import admin
##from SimmiFoundation.fundraisers.models.ngo import ngo

from .models.ngo import ngo
from .models.fundraisers_medical import Fundraisers_medical
from .models.fundraisers_others import Fundraiser_others
from .models.campaign import Campaign
# Register your models here.

admin.site.register(Fundraisers_medical)
admin.site.register(ngo)
admin.site.register(Fundraiser_others)
admin.site.register(Campaign)