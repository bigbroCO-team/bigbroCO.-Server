from django.db import transaction
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from cart.models import Cart
from cart.serializers import CartSerializer


# Create your views here.
class CartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object) -> Response:
        cart = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: object) -> Response:
        for obj in request.data:
            obj['user'] = request.user.id
            try:
                cart = Cart.objects.get(user=request.user, option=obj['option'])
                obj['count'] += cart.count
                serializer = CartSerializer(instance=cart, data=obj)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Cart.DoesNotExist:
                serializer = CartSerializer(data=obj)
                serializer.is_valid(raise_exception=True)
                serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    @transaction.atomic
    def delete(self, request: object, id: int) -> Response:
        cart = Cart.objects.get(id=id)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
