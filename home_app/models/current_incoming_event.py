from django.db import models
#EVENT MODEL
class Current_incoming_event(models.Model):
    #FUNCTION FOR STORE IMAGE SEPERATELY WITH EVENT IMAGE
    def nameFile(instance,filename):             
     return '/'.join(['EVENT_IMAGE',str(instance.event_name),filename])

    event_img=models.ImageField(upload_to=nameFile)
    event_name=models.CharField(max_length=50)
    about_event=models.CharField(max_length=300)