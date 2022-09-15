from django.db import models
import datetime
class Fundraisers_medical(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['MEDICAL_FUNDRAISER', str(instance.patient_name), filename])

    camera_file=models.ImageField(upload_to=nameFile)
    cover_photo=models.ImageField(upload_to=nameFile)
    estimation_letter=models.FileField(upload_to=nameFile)
    medical_bill=models.FileField(upload_to=nameFile)
    medical_reports=models.FileField(upload_to=nameFile)

    patient_name=models.CharField(max_length=50)
    patient_age = models.IntegerField()
    patient_address = models.CharField(max_length=250)
    beneficiary = models.CharField(max_length=50)
    relation=models.CharField(max_length=50)

    phone=models.CharField(max_length=15)
    email=models.EmailField()
    target_amount=models.IntegerField()
    end_date = models.DateField()

    hospital_name = models.CharField(max_length=50)
    hospital_address = models.CharField(max_length=250)

    medical_ailment = models.CharField(max_length=50)
    current_situation_details = models.CharField(max_length=500)
    doctor_name = models.CharField(max_length=50)
    doctor_number=models.IntegerField()
    hospital_number=models.IntegerField()
    fundraiser_title = models.CharField(max_length=50)
    fundraiser_description = models.CharField(max_length=600)

    current_amount_raised = models.IntegerField()
