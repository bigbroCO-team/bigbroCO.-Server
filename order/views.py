# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from order.models import Order
from order.serializers import ProductItemSerializer


class CreateOrderListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: object) -> Response:
        serializer = ProductItemSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        Order.objects.create()
