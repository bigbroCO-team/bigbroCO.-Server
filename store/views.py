from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Cart, Wishlist
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object, pk: None) -> Response:
        cart = Cart.objects.filter(pk=pk, customer=request.user) if pk else Cart.objects.filter(customer=request.user)
