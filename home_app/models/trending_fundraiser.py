from django.db import models
#TRENDING FUNDRAISER MODEL
class Trending_fundraisers(models.Model):
    def nameFile(instance,filename):             
     return '/'.join(['TRENDING_FUNDRAISER_IMAGE',str(instance.fundraiser_name),filename])
    fundraiser_image=models.ImageField(upload_to=nameFile)
    fundraiser_name=models.CharField(max_length=50)
    fundraise_by_name=models.CharField(max_length=50)
    fundraise_by_image=models.ImageField(upload_to=nameFile)
    fund_amout_raise=models.IntegerField()
    fund_amount_target=models.IntegerField()
    fund_start_date=models.DateField(null=True)
    fund_end_date=models.DateField(null=True)
    fundraiser_support=models.IntegerField(null=True)