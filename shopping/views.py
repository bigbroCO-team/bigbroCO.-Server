from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Cart, Wishlist
from .serializers import WishlistSerializer, CartSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
class CartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object, pk: str = None) -> Response:
        if pk:
            cart = Cart.objects.filter(pk=pk, customer=request.user)
        else:
            cart = Cart.objects.filter(customer=request.user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: object) -> Response:
        serializer = CartSerializer(data=request.data)
        serializer.initial_data['customer'] = request.user.id
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request: object, pk: str):
        cart = get_object_or_404(Cart, customer=request.user, id=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WishListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object, pk: str = None) -> Response:
        if pk:
            wishlist = Wishlist.objects.get(pk=pk, customer=request.user)
        else:
            wishlist = Wishlist.objects.filter(customer=request.user)
        serializer = WishlistSerializer(instance=wishlist, many=True)
        return Response(serializer.data)

    def post(self, request: object) -> Response:
        serializer = WishlistSerializer(data=request.data)
        serializer.initial_data['customer'] = request.user.id
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: object, pk: str) -> Response:
        wishlist = get_object_or_404(Wishlist, id=pk, customer=request.user)
        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
