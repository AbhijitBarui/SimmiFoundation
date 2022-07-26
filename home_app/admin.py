from django.contrib import admin

# Register your models here.

from django.contrib import admin

# from home_app.models.current_incoming_event import Current_incoming_event
# from home_app.models.our_partners import Our_partners, Our_partners
# from home_app.models.our_success_story import OUR_success_story, Our_success_story
# from home_app.models.our_volunteers import OUR_volunteers, Our_volunteers
# from home_app.models.trending_fundraiser import TRENDING_fundraisers, Trending_fundraisers
# from home_app.models.what_people_say import WHAT_people_say
from .models import *
from home_app.models import *

#TRENDING FUNDRAISER ADMIN MODIFICATION
class trending_fundAdmin(admin.ModelAdmin):
    list_display=['fundraiser_image','fundraiser_name','fundraise_by_name','fundraise_by_image','fund_amout_raise','fund_amount_target','fund_start_date','fund_end_date'
                
    ]
#CURRENT AND INCOMING EVENT ADMIN MODIFICATION
class event(admin.ModelAdmin):
    list_display=['event_img','event_name','about_event']

class Event(admin.ModelAdmin):
    list_display=['event_img','event_name','event_location','event_date']

#WHAT PEOPLE SAY ADMIN MODIFICATION
class people_say(admin.ModelAdmin):
    list_display =['person_name','person_image','person_review']

# OUR SUCCESS STORY ADMIN MODIFICATION
class success_story(admin.ModelAdmin):
    list_display =['success_img','success_heading','about_success']

# OUR VOLUNTEERS ADMIN MODIFICATION
class volunteers(admin.ModelAdmin):
    list_display =['volunteer_img','volunteer_name','about_volunteer','volunteer_instagrm_id','volunteer_twitter_id','volunteer_linkdin_id','volunteer_facebook_id']


# OUR PARTNERS ADMIN MODIFICATION
class partners(admin.ModelAdmin):
    list_display =['partner_logo','partner_name']

# Register your models here.
admin.site.register(carousel)   # CAROSOUL REGISTER 
admin.site.register(Trending_fundraisers,trending_fundAdmin)     # TRENDING FUNDRAISER REGISTER
admin.site.register(Current_incoming_event,event)                 # CURRENT AND INCOMING EVENT REGISTER
admin.site.register(Incoming_event,Event)
admin.site.register(What_people_say,people_say)               # WHAT PEOPLE SAY  REGISTER
admin.site.register(Our_success_story,success_story)            # OUR SUCCESS STORY REGISTER
admin.site.register(Our_volunteers,volunteers)                  # OUR VOLUNTEEERS REGISTER
admin.site.register(Our_partners,partners)                   # OUR  PARTNERS REGISTER           
 
