from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
from .serializers import TransactionSerializer
import json
import hmac
import hashlib

@method_decorator(csrf_exempt, name='dispatch')
class PaystackWebhook(APIView):
    def post(self, request, *args, **kwargs):
        secret_key = 'sk_test_d839813fcae431abc36f11cec202e131f030e09c'
        paystack_signature = request.headers.get('x-paystack-signature')
        payload = request.body

        generated_signature = hmac.new(
            secret_key.encode(),
            payload,
            hashlib.sha512
        ).hexdigest()

        if generated_signature != paystack_signature:
            return Response({'error': 'Invalid signature'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            event = json.loads(request.body).get('event')
            if event == 'charge.success':
                data = json.loads(request.body).get('data')
                if data and data['status'] == 'success':
                    transaction_data = {
                        'transaction_id': data.get('id'),
                        'amount': data.get('amount') / 100,  # Paystack amounts are in kobo
                        'currency': data.get('currency'),
                        'customer_email': data.get('customer', {}).get('email'),
                        'status': 'success'
                    }

                    serializer = TransactionSerializer(data=transaction_data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GetAllTransaction(APIView):
    def get(self,request):
        payment = Transaction.objects.all()
        data = TransactionSerializer(payment, many=True)
        return Response(data.data)