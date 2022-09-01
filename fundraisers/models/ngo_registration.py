from django.db import models

type_of_ngo=(
    ('trust registered','trust registered'),
    ('society registered','society registered'),
    ('section 8 comapany registered','section 8 coampany registered'),
)
approve_status=(
    ('approved','approved'),
    ('declined','declined'),
    ('pending','pending'),
)
class ngo_registration(models.Model):
    organisation_type=models.CharField(max_length=30,choices=type_of_ngo,default='trust registered')
    def nameFile(instance,filename):             
     return '/'.join(['NGO_REGISTRATION',str(instance.organisation_name),filename])
    ##details
    organisation_name=models.CharField(max_length=30,unique=True,blank=False)
    email=models.EmailField()
    phone_number=models.IntegerField(null=True)
    problem_addressing=models.CharField(max_length=160,null=True)
    valid_status=models.CharField(max_length=8,null=False,blank=False,choices=approve_status,default='pending')
    organisation_address=models.CharField(max_length=200)

    ##proofs from the ngo
    photo=models.FileField(upload_to=nameFile,null=True)

    ##media links 
    wesite_link=models.URLField(blank=True,null=True)
    facebook_link=models.URLField(blank=True,null=True)
    instagram_link=models.URLField(blank=True,null=True)
    linkedin_link=models.URLField(blank=True,null=True)
    twitter_link=models.URLField(blank=True,null=True)

    ##tax exception
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    
    ##ngo_certificates
     ##certificates for society registered ngo
    registration_certificate=models.FileField(upload_to=nameFile,null=True,blank=True)##for trust type ngo also
    memorandum=models.FileField(upload_to=nameFile,null=True,blank=True)
    ##certificates for trust registered ngo
    trust_deed=models.FileField(upload_to=nameFile,null=True,blank=True)
    ##certificates for section 8 comapny registered ngo
    section_8_license=models.FileField(upload_to=nameFile,null=True,blank=True)
    article_of_association=models.FileField(upload_to=nameFile,null=True,blank=True)##AOA
    memorandum_of_association=models.FileField(upload_to=nameFile,null=True,blank=True)##MOA
    ##extra documents
    document1_name=models.CharField(max_length=20,blank=True,null=True)
    document1=models.FileField(upload_to=nameFile,null=True,blank=True)
    document2_name=models.CharField(max_length=20,blank=True,null=True)
    document2=models.FileField(upload_to=nameFile,null=True,blank=True)
    document3_name=models.CharField(max_length=20,blank=True,null=True)
    document3=models.FileField(upload_to=nameFile,null=True,blank=True)
    document4_name=models.CharField(max_length=20,blank=True,null=True)
    document4=models.FileField(upload_to=nameFile,null=True,blank=True)
   

    def __str__(self):
        return self.organisation_name