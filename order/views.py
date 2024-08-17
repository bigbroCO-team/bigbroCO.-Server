# Create your views here.
from django.db import transaction
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


