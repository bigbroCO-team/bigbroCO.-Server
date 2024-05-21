from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


# Create your views here.
class ProductView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: object) -> Response:
        products = Product.objects.all()
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data)

    def post(self, request: object) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CategoryView(APIView):
    def get(self, request: object) -> Response:
        categories = Category.objects.all()
        serializer = CategorySerializer(instance=categories, many=True)
        return Response(serializer.data)
