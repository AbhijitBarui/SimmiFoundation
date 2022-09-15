from http.server import BaseHTTPRequestHandler
from django.db import models
#OUR  VOLUNTEERS MODEL 
class Our_volunteers(models.Model):
    def nameFile(instance,filename):             
     return '/'.join(['OUR_VOLUNTEERS_IMAGE',str(instance.volunteer_name),filename])
    volunteer_img=models.ImageField(upload_to=nameFile)
    volunteer_name=models.CharField(max_length=100)
    about_volunteer=models.TextField(max_length=300)
    volunteer_instagrm_id=models.URLField(max_length=300 ,blank=True,null=True)
    volunteer_twitter_id=models.URLField(max_length=300, blank=True,null=True)
    volunteer_linkdin_id=models.URLField(max_length=300 , blank=True,null=True)
    volunteer_facebook_id=models.URLField(max_length=300 , blank=True,null=True)