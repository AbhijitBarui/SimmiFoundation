from django.db import models

beneficiarysex=(
    ('Male','Male'),
    ('Female','Female'),
    ('others','others'),
)

class Fundraiser_others(models.Model):
    def nameFile(instance,filename):
        return '/'.join(['FUNDRAISER_OTHERS',str(instance.beneficiary_name),filename])

    name=models.CharField(max_length=25)
    contact_number=models.PositiveIntegerField()
    email_id=models.EmailField()
    street_address=models.CharField(max_length=60)
    street_address1=models.CharField(max_length=50,blank=True)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    postal_code=models.IntegerField()

    ##beneficiary details
    to_whom_fund_raised=models.CharField(max_length=20)
    beneficiary_name=models.CharField(max_length=20)
    beneficiary_contact_number=models.IntegerField()
    beneficiary_age=models.IntegerField()
    beneficiary_sex=models.CharField(max_length=10,choices=beneficiarysex)
    beneficiary_address=models.CharField(max_length=50)
    beneficiary_address1=models.CharField(max_length=50,blank=True)
    beneficiary_city=models.CharField(max_length=15)
    beneficiary_state=models.CharField(max_length=15)
    beneficiary_postalcode=models.IntegerField()
    title_of_campaign=models.TextField(max_length=100,unique=True)
    beneficiary_story=models.TextField(max_length=300)

    #taxstatus
    tax_Status=models.CharField(max_length=20,null=True)

    #checkbox
    update_check=models.BooleanField(default=False,editable=True)
    terms_check=models.BooleanField(default=False,editable=True)

    ##documents proofs 
    video=models.FileField(upload_to=nameFile,blank=True)
    beneficiary_photo=models.ImageField(upload_to=nameFile)
    document=models.FileField(upload_to=nameFile)


    ##details of campaign
    target_amount=models.IntegerField()
    end_date=models.CharField(max_length=10)



