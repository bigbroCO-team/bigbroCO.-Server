from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from product.models import Product
from product.serializers import ImageSerializer, ProductSerializer


# Create your views here.
class ProductView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get(self, request: object) -> Response:
        products = Product.objects.all()
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
