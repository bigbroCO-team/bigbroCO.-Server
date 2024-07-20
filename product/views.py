from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
class ProductView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [AllowAny]

    def get(self, request: object) -> Response:
        products = Product.objects.all()
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAdminView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request: object) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request: object, id: int) -> Response:
        product = Product.objects.get(pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
