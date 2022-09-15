from django.db import models
#OUR  PARTNERS MODEL 
class Our_partners(models.Model):
    #FUNCTION FOR STORE IMAGE SEPERATELY WITH PARTNER  IMAGE
    def nameFile(instance,filename):             
     return '/'.join(['OUR_PARTNER_IMAGE',str(instance.partner_name),filename])
    partner_logo=models.ImageField(upload_to=nameFile)
    partner_name=models.CharField(max_length=100)
   