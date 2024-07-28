import logging

from django.db import transaction
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
        print(product.query)
        serializer = ProductSerializer(instance=product, many=False)
        print(serializer.data)
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

    @transaction.atomic
    def post(self, request: object) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def put(self, request: object, id: int) -> Response:
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def delete(self, request: object, id: int) -> Response:
        product = get_object_or_404(Product, id=id)
        product.on_sale = False
        product.save()
        return Response(status=status.HTTP_200_OK)


class UploadView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    @transaction.atomic
    def post(self, request):
        image = request.FILES.get('file', None)
        url = s3.upload(image)
        return Response({'url': url}, status=status.HTTP_201_CREATED)
