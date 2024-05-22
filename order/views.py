from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import OrderSerializer
from order.models import Order
from django.shortcuts import get_object_or_404


# Create your views here.

# Admin View
class OrderAdminView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: object) -> Response:
        order = Order.objects.all()
        serializer = OrderSerializer(instance=order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: object) -> Response:
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, pk) -> Response:
        order = get_object_or_404(Order, id=pk)
        serializer = OrderSerializer(Order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: object, pk) -> Response:
        order = get_object_or_404(Order, id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
