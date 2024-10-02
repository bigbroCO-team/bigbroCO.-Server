from django.db import transaction
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from src.app.client.cart.models import Cart
from src.app.client.cart.serializers import CartSerializer, CartSerializerWithoutUser


@extend_schema_view(
    get=extend_schema(
        summary='Get my cart list API',
        description='내 카트를 조회합니다',
        responses=CartSerializer
    ),
    post=extend_schema(
        summary='Create a new cart API',
        description='내 카트에 상품을 추가합니다.',
        request=CartSerializer
    ),
    delete=extend_schema(
        summary='Delete a cart API',
        description='내 카트를 삭제합니다.',
        parameters=[
            OpenApiParameter(name='id', description='Cart id', required=True, type=OpenApiTypes.INT),
        ]
    )
)
class CartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object) -> Response:
        cart = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: object) -> Response:
        serializer = CartSerializerWithoutUser(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request: object, pk: int) -> Response:
        cart = Cart.objects.filter(user=request.user, id=pk)
        cart.delete()
        return Response(status=status.HTTP_200_OK)