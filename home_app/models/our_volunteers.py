from django.db import models
#OUR  VOLUNTEERS MODEL 
class Our_volunteers(models.Model):
    def nameFile(instance,filename):             
     return '/'.join(['OUR_VOLUNTEERS_IMAGE',str(instance.volunteer_name),filename])
    volunteer_img=models.ImageField(upload_to=nameFile)
    volunteer_name=models.CharField(max_length=100)
    about_volunteer=models.TextField(max_length=300)