from django.db import models
#TRENDING FUNDRAISER MODEL
class What_people_say(models.Model):
    def nameFile(instance,filename):             
     return '/'.join(['WHAT_PEOPLE_SAY_IMAGE',str(instance.person_name),filename])
    person_name=models.CharField(max_length=50)
    person_image=models.ImageField(upload_to=nameFile)
    person_review=models.TextField(max_length=500)
