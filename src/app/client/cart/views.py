from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

from src.app.client.cart.models import Cart
from src.app.client.cart.serializers import CartSerializer


# Create your views here.
class CartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object) -> Response:
        cart = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def post(self, request: object) -> Response:
        serializer = CartSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)
