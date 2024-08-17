# Create your views here.
import base64
import json

import requests
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from order.models import Order, OrderItem
from order.serializers import OrderListSerializer, OrderSerializer


class OrderListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object) -> Response:
        order = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(instance=order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: object) -> Response:
        serializer = OrderListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)


class TossPaymentsView(APIView):
    @transaction.atomic
    def get(self, request: object) -> Response:
        orderId = request.GET.get('orderId')
        tossOrderId = request.GET.get('tossOrderId')
        amount = request.GET.get('amount')
        paymentKey = request.GET.get('paymentKey')

        order = get_object_or_404(Order, id=orderId)
        if order.total != amount:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        url = "https://api.tosspayments.com/v1/payments/confirm"
        secertkey = "test_sk_zXLkKEypNArWmo50nX3lmeaxYG5R"
        userpass = secertkey + ':'
        encoded_u = base64.b64encode(userpass.encode()).decode()

        headers = {
            "Authorization": "Basic %s" % encoded_u,
            "Content-Type": "application/json"
        }

        params = {
            "orderId": orderId,
            "amount": amount,
            "paymentKey": paymentKey,
        }

        res = requests.post(url, data=json.dumps(params), headers=headers)
        resjson = res.json()
        pretty = json.dumps(resjson, indent=4)

        if res.status_code == 200:
            # Todo -> order status
            order.order_id = tossOrderId
            order.payment_key = paymentKey
            order.total_amount = amount
            order.save()

            respaymentKey = resjson["paymentKey"]
            resorderId = resjson["orderId"]
            rescardcom = resjson["card"]["company"]

            return Response({
                "res": pretty,
                "paymentKey": respaymentKey,
                "orderId": resorderId,
                "cardcom": rescardcom

            }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)