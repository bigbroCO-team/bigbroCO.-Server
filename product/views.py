from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from product.models import Product, Category, Size, Rating
from product.serializers import ProductSerializer, CategorySerializer, SizeSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class ProductView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: object, pk=None) -> Response:
        if pk:
            product = Product.objects.get(id=pk)
        else:
            product = Product.objects.all()
        serializer = ProductSerializer(instance=product, many=False if pk else True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: object) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, pk: int) -> Response:
        products = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(products, data=request.data)
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

    def get(self, request: object, pk=None) -> Response:
        if pk:
            category = Category.objects.get(id=pk)
        else:
            category = Category.objects.all()
        serializer = CategorySerializer(instance=category, many=True)
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
        product = Product.objects.filter(category=pk)
        if product.exists():
            return Response({'error', 'Product exists'}, status=status.HTTP_400_BAD_REQUEST)
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
        product = Product.objects.filter(size=pk)
        if product.exists():
            return Response({'error', 'Product exists'}, status=status.HTTP_400_BAD_REQUEST)

        size = get_object_or_404(Size, id=pk)
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
