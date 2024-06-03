from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Address
from .serializers import AddressSerializer
from common.models import Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from order.models import Order
from django.shortcuts import get_object_or_404


# Create your views here.
class AddressView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object, pk=None) -> Response:
        if pk:
            address = Address.objects.filter(customer=request.user, id=pk)
        else:
            address = Address.objects.filter(customer=request.user)

        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: object) -> Response:
        print("start")
        user = Customer.objects.get(username=request.user.username)

        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.validated_data['customer'] = user

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, pk: int) -> Response:
        orders = Order.objects.filter(customer=request.user, address=pk, status__in=('SHIPPED', 'PROCESSING', 'PENDING'))
        if orders.exists():
            return Response('Processing order exists', status=status.HTTP_400_BAD_REQUEST)

        address = get_object_or_404(Address, customer=request.user, id=pk)
        serializer = AddressSerializer(address, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: object, pk: int) -> Response:
        orders = Order.objects.filter(customer=request.user, address=pk, status__in=('SHIPPED', 'PROCESSING', 'PENDING'))
        if orders.exists():
            return Response('Processing order exists', status=status.HTTP_400_BAD_REQUEST)
        address = get_object_or_404(Address, id=pk, customer=request.user)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
