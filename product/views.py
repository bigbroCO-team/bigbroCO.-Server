from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer, SizeSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class ProductView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: object) -> Response:
        products = Product.objects.all()
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: object) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, pk: int) -> Response:
        products = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(Product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: object, pk: int) -> Response:
        products = get_object_or_404(Product, id=pk)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: object) -> Response:
        categories = Category.objects.all()
        serializer = CategorySerializer(instance=categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: object) -> Response:
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, pk: int) -> Response:
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: object, pk: int) -> Response:
        category = get_object_or_404(Category, id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SizeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: object) -> Response:
        size = Size.objects.all()
        serializer = SizeSerializer(instance=size, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: object) -> Response:
        serializer = SizeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, pk: int) -> Response:
        size = get_object_or_404(Size, id=pk)
        serializer = SizeSerializer(Size, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: object, pk: int) -> Response:
        size = get_object_or_404(Size, id=pk)
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
