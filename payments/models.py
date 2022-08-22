from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus

# Create your models here.
class RazorpayPayment(models.Model):
    currency = models.CharField(max_length=100)
    amount = models.IntegerField()
    tip = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    email=models.CharField(max_length=100)
    indian=models.BooleanField()
    anonymously=models.BooleanField()

    provider_order_id = models.CharField(_("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(_("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(_("Signature ID"), max_length=128, null=False, blank=False
    )

    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )