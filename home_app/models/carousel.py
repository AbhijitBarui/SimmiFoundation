from django.db import models
#CAROUSEL MODEL
class carousel(models.Model):
    carousel_img=models.ImageField(upload_to='carousel_image')