from django.db import models

class Fundraisers_medical(models.Model):
    patient_name=models.CharField(max_length=50)
    # benificiary=models.CharField(max_length=50)
    relation=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    target_amount=models.IntegerField()
    # end_date=models.DateField()
    patient_age=models.IntegerField()
    patient_photo=models.ImageField(upload_to='uploads/patient_photo/')
    medical_ailment=models.CharField(max_length=50)
    current_situation_details=models.CharField(max_length=500)
    hospital_name=models.CharField(max_length=50)
    hospital_address=models.CharField(max_length=250)
    patient_address=models.CharField(max_length=250)
    doctor_name=models.CharField(max_length=50)
    fundraiser_title=models.CharField(max_length=50)
    fundraiser_description=models.CharField(max_length=600)
    medical_documents=models.ImageField(upload_to='uploads/medical_document/')

