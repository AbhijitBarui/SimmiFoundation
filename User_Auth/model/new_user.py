from django.db import models

from datetime import datetime
# import datetime

now=datetime.now()
time_sting= now.strftime("%H:%M:%S")
dt_sting= now.strftime("%Y-%m-%d")


class newuser(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
  

    

    #cpassword=models.CharField(max_length=100)