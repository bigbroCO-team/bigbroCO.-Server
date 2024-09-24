from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from src.app.address.models import Address
from src.app.address.serializers import AddressSerializer
from src.app.user.models import User


# Create your views here.
class AddressView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object, id: int = None) -> Response:
        if id:
            address = get_object_or_404(Address, pk=id, user=request.user)
            serializer = AddressSerializer(address)
        else:
            address = Address.objects.filter(user=request.user)
            serializer = AddressSerializer(address, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: object) -> Response:
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=User.objects.get(id=request.user.id)
        )
        return Response(status=status.HTTP_201_CREATED)

    @transaction.atomic
    def put(self, request: object, id: int) -> Response:
        address = Address.objects.get(id=id, user=request.user)
        serializer = AddressSerializer(instance=address, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    @transaction.atomic
    def delete(self, request: object, id: int) -> Response:
        address = get_object_or_404(Address, id=id, user=request.user)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
