from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from config.settings import PAYMENTS_KEY
from order.models import Order
from order.serializers import OrderSerializer
from shopping.models import Cart
from shopping.serializers import CartSerializer
from django.shortcuts import get_object_or_404
import base64
import requests
import json


# Create your views here.
class PaymentSuccessView(APIView):
    def get(self, request: object) -> Response:
        url = 'https://api.tosspayments.com/v1/payments/confirm'
        secret = PAYMENTS_KEY + ':'
        encryptedSecretKey: str = base64.b64encode(secret.encode()).decode()

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
        if r.status_code == 200:
            key = r.json()['paymentKey']
            orderid = r.json()['orderId']
            total = r.json()['total']
        else:
            code = r.json()['code']
            msg = r.json()['message']
