from django.db import models
#OUR SUCCESS STORY
class Our_success_story(models.Model):
    def nameFile(instance,filename):             
     return '/'.join(['OUR_SUCCESS_IMAGE',str(instance.success_heading),filename])
    success_img=models.ImageField(upload_to=nameFile)
    success_heading=models.CharField(max_length=100)
    about_success=models.CharField(max_length=300)