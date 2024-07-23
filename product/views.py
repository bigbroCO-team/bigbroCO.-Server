from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from product import s3
from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
class ProductListView(APIView):
    def get(self, request: object) -> Response:
        category = request.query_params.get('category', None)
        product = Product.objects.filter(category=category)
        serializer = ProductSerializer(instance=product, many=True)
        return Response(serializer.data)


class GetProductByIdView(APIView):
    def get(self, request: object, id: int) -> Response:
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(instance=product)
        serialized_data = serializer.data

        if not serialized_data['on_sale']:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not serialized_data['open_stock']:
            for option in serialized_data['options']:
                del option['stock']

        return Response(serialized_data, status=status.HTTP_200_OK)


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


class UploadView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        image = request.FILES.get('file', None)
        url = s3.upload(image)
        return Response({'url': url}, status=status.HTTP_201_CREATED)
