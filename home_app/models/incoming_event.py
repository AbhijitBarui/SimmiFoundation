from django.db import models
#EVENT MODEL
class Incoming_event(models.Model):
    #FUNCTION FOR STORE IMAGE SEPERATELY WITH EVENT IMAGE
    def nameFile(instance,filename):             
     return '/'.join(['EVENT_IMAGE',str(instance.event_name),filename])

    event_img=models.ImageField(upload_to=nameFile)
    event_name=models.CharField(max_length=100)
    event_location=models.CharField(max_length=300)
    event_date=models.DateField()