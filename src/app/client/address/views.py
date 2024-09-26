from django.db import transaction
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from src.app.client.address.models import Address
from src.app.client.address.serializers import AddressSerializer


@extend_schema_view(
    get=extend_schema(
        summary='Get my address',
        description='자신의 집 주소들 불러오기',
        responses=AddressSerializer
    ),
    post=extend_schema(
        summary='Create a new address',
        description='집 주소 업로드',
        request=AddressSerializer,
        responses=AddressSerializer
    )
)
class AddressView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object) -> Response:
        address = Address.objects.filter(user=request.user)
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: object) -> Response:
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)


@extend_schema_view(
    put=extend_schema(
        summary='Update my address API',
        description='자신의 집 주소 업데이트',
        request=AddressSerializer,
        responses=AddressSerializer
    ),
    delete=extend_schema(
        summary='Delete my address API',
        description='자신의 집 주소 삭제'
    )
)
class AddressDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request: object, pk: int) -> Response:
        address = get_object_or_404(Address, pk=pk, user=request.user)
        serializer = AddressSerializer(address, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request: object, pk: int) -> Response:
        address = get_object_or_404(Address, pk=pk, user=request.user)
        address.delete()
        return Response(status=status.HTTP_200_OK)