from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *
from home_app.models import trending_fundraisers

#TRENDING FUNDRAISER ADMIN MODIFICATION
class trending_fundAdmin(admin.ModelAdmin):
    list_display=['fundraiser_image','fundraiser_name','fundraise_by_name','fundraise_by_image','fund_amout_raise','fund_amount_target','fund_start_date','fund_end_date'
                
    ]
#CURRENT AND INCOMING EVENT ADMIN MODIFICATION
class event(admin.ModelAdmin):
    list_display=['event_img','event_name','about_event']

#WHAT PEOPLE SAY ADMIN MODIFICATION
class What_people_say(admin.ModelAdmin):
    list_display =['person_name','person_image','person_review']

# OUR SUCCESS STORY ADMIN MODIFICATION
class Our_success_story(admin.ModelAdmin):
    list_display =['success_img','success_heading','about_success']

# OUR VOLUNTEERS ADMIN MODIFICATION
class Our_volunteers(admin.ModelAdmin):
    list_display =['volunteer_img','volunteer_name','about_volunteer']


# OUR PARTNERS ADMIN MODIFICATION
class Our_partners(admin.ModelAdmin):
    list_display =['partner_logo','partner_name']

# Register your models here.
admin.site.register(carousel)   # CAROSOUL REGISTER 
admin.site.register(trending_fundraisers,trending_fundAdmin)     # TRENDING FUNDRAISER REGISTER
admin.site.register(current_incoming_event,event)                 # CURRENT AND INCOMING EVENT REGISTER
admin.site.register(what_people_say,What_people_say)               # WHAT PEOPLE SAY  REGISTER
admin.site.register(our_success_story,Our_success_story)            # OUR SUCCESS STORY REGISTER
admin.site.register(our_volunteers,Our_volunteers)                  # OUR VOLUNTEEERS REGISTER
admin.site.register(our_partners,Our_partners)                   # OUR  PARTNERS REGISTER           
 
