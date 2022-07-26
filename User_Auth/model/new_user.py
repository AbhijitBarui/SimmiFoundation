from django.db import models


class newuser(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    Phone=models.IntegerField(null=True)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)