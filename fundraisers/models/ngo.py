from django.db import models

class ngo(models.Model):
    ##ngo_certificates
    regulation_certificate=models.ImageField(upload_to='uploads/ngo_proofs/regulation_certificate',null=True)
    certificate_12A=models.ImageField(upload_to='uploads/ngo_proofs/certificate_12A',null=True)
    valid_status=models.BooleanField(default=False)
    type_of_ngo_certificate=models.TextField(max_length=50)
    license_number=models.CharField(max_length=50)
    ##proofs from the ngo
    title=models.CharField(max_length=100)
    videos=models.FileField(upload_to='uploads/ngo_proofs/ngo_videos',null=True,blank=True)
    description=models.TextField(max_length=200)
    photo1=models.ImageField(upload_to='uploads/ngo_proofs/ngo_photos',null=True,blank=True)
    photo2=models.ImageField(upload_to='uploads/ngo_proofs/ngo_photos',null=True,blank=True)
    photo2=models.ImageField(upload_to='uploads/ngo_proofs/ngo_photos',null=True,blank=True)
    photo3=models.ImageField(upload_to='uploads/ngo_proofs/ngo_photos',null=True,blank=True)
    photo4=models.ImageField(upload_to='uploads/ngo_proofs/ngo_photos',null=True,blank=True)
    photo5=models.ImageField(upload_to='uploads/ngo_proofs/ngo_photos',null=True,blank=True)
    address=models.CharField(max_length=200)
    contact=models.IntegerField()
    email=models.EmailField()
    media_links=models.URLField(blank=True)
    ##tax exception
    created=models.CharField(max_length=100)
    updated=models.CharField(max_length=100)