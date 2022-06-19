from django.contrib import admin
##from SimmiFoundation.fundraisers.models.ngo import ngo

from .models.ngo import ngo
from .models.fundraisers_medical import Fundraisers_medical
# Register your models here.

admin.site.register(Fundraisers_medical)
admin.site.register(ngo)
