from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from config.settings import PAYMENTS_KEY
import base64
import requests
import json


# Create your views here.
class PaymentSuccessView(APIView):
    def get(self, request: object) -> Response:
        secret = PAYMENTS_KEY + ':'
        encryptedSecretKey: str = base64.b64encode(secret.encode()).decode()
        url = 'https://api.tosspayments.com/v1/payments/confirm'

        headers = {
            "Authorization": "Basic %s" % encryptedSecretKey,
            "Content-Type": "application/json"
        }
        params = {
            "orderId": request.data.get('orderId'),
            "amount": request.data.get('amount'),
            "paymentKey": request.data.get('paymentKey'),
        }

        r = requests.post(url, headers=headers, data=json.dumps(params))
        # if r.status_code == 200:


