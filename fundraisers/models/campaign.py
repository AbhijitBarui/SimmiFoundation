from django.db import models


class Campaign(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['MEDICAL_FUNDRAISER', str(instance.title), filename])

    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    phone=models.IntegerField()
    relation=models.CharField(max_length=150)
    city=models.CharField(max_length=100)
    raising_for=models.CharField(max_length=200)

    title=models.CharField(max_length=250)
    aim=models.IntegerField()
    end_date=models.DateField()
    main_pic=models.ImageField(upload_to=nameFile)
    cover_photo=models.ImageField(upload_to=nameFile)
    story=models.CharField(max_length=750)
    category_tag=models.CharField(max_length=50)

    current_amount_raised=models.IntegerField(blank=True, null=True)

