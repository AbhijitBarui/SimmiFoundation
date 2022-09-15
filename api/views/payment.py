import json
import os
import razorpay
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from payments.constants import PaymentStatus
from decouple import config
from payments.models import RazorpayPayment

# Get Razorpay Key id and secret for authorizing razorpay client.
#RAZOR_KEY = os.getenv(config('RAZORPAY_KEY'), None)
#RAZOR_SECRET = os.getenv(config('RAZORPAY_SECRET'), None)

# Creating a Razorpay Client instance.
#razorpay_client = razorpay.Client(auth=(config('RAZORPAY_KEY'), config('RAZORPAY_SECRET')))


class PaymentView(APIView):
    """
    APIView for Creating Razorpay Order.
    :return: list of all necessary values to open Razorpay SDK
    """

    http_method_names = ('post',)

    @staticmethod
    def post(request, *args, **kwargs):
        # Take Order Id from frontend and get all order info from Database.
        # order_id = request.data.get('order_id', None)



        # currency = models.CharField(max_length=100)
        # amount = models.IntegerField()
        # tip = models.IntegerField(default=0)
        # name = models.CharField(max_length=200)
        # country_code = models.CharField(max_length=10)
        # phone_number = models.IntegerField()
        # email = models.CharField(max_length=100)
        # indian = models.BooleanField()
        # anonymously = models.BooleanField()

        # Here We are Using Static Order Details for Demo.
        # name = "Swapnil Pawar"
        # amount = 400

        data = request.data
        # Create Order
        a=(int(data['amount'])+int(data['tip']))*100
        razorpay_order = razorpay_client.order.create(
            {"amount": a , "currency": data['currency']}
        )

        # Save the order in DB
        order = RazorpayPayment.objects.create(
            name=data['name'], currency=data['currency'], tip=data['tip'], amount=data['amount'],
            country_code=data['country_code'], phone_number=data['phone_number'], email=data['email'],
            indian=data['indian'], anonymously=data['anonymously'], provider_order_id=razorpay_order["id"]
        )

        response_data = {
            "orderId": razorpay_order["id"],
        }

        # save order Details to frontend
        return Response(response_data, status=status.HTTP_200_OK)





class CallbackView(APIView):
    """
    APIView for Verifying Razorpay Order.
    :return: Success and failure response messages
    """

    @staticmethod
    def post(request, *args, **kwargs):

        # getting data form request
        response = request.data

        """
            if razorpay_signature is present in the request 
            it will try to verify
            else throw error_reason
        """
        if "razorpay_signature" in response:

            # Verifying Payment Signature
            data = razorpay_client.utility.verify_payment_signature(response)

            # if we get here True signature
            if data:
                payment_object = RazorpayPayment.objects.get(provider_order_id=response[
                    'razorpay_order_id'])
                # razorpay_payment = RazorpayPayment.objects.get(order_id=response['razorpay_order_id'])
                payment_object.status = PaymentStatus.SUCCESS
                payment_object.payment_id = response['razorpay_payment_id']
                payment_object.signature_id = response['razorpay_signature']
                payment_object.save()

                return Response({'status': 'Payment Done'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'Signature Mismatch!'}, status=status.HTTP_400_BAD_REQUEST)

        # Handling failed payments
        else:
            error_code = response['error[code]']
            error_description = response['error[description]']
            error_source = response['error[source]']
            error_reason = response['error[reason]']
            error_metadata = json.loads(response['error[metadata]'])
            razorpay_payment = RazorpayPayment.objects.get(provider_order_id=error_metadata['order_id'])
            razorpay_payment.payment_id = error_metadata['payment_id']
            razorpay_payment.signature_id = "None"
            razorpay_payment.status = PaymentStatus.FAILURE
            razorpay_payment.save()

            error_status = {
                'error_code': error_code,
                'error_description': error_description,
                'error_source': error_source,
                'error_reason': error_reason,
            }

            return Response({'error_data': error_status}, status=status.HTTP_401_UNAUTHORIZED)
