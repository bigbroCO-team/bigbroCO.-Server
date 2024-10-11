from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

from product.models import Product
from product.serializers import ProductSerializer

@extend_schema_view(
    get=extend_schema(
        summary='Product detail',
        description='id값의 Product 조회',
        responses=ProductSerializer
    )
)
class ProductDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get(self, request: object, pk: int) -> Response:
        product = get_object_or_404(Product, pk=pk, is_active=True)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

@extend_schema_view(
    get=extend_schema(
        summary='Product list by category',
        description='category를 기준으로 product 조회',
        responses=ProductSerializer
    )
)
class ProductListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get(self, request: object) -> Response:
        category: str = request.GET.get('category', 'BIGBRO')
        products = Product.objects.filter(category__in=category, is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)