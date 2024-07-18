from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer


class ProductView(APIView):
    def post(self, request: object) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, id: int) -> Response:
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: object, id: int) -> Response:
        Product.objects.get(pk=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
