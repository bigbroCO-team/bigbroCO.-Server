from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from order.models import Order
from product.models import Product, Rating
from product.serializers import ProductSerializer, RatingSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Avg


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


class RatingView(APIView):
    def get(self, request: object, pk: int) -> Response:
        rating = Rating.objects.filter(id=pk)
        if not rating.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        avg = rating.aggregate(Avg('rating'))
        return Response(avg)

    def post(self, request: object) -> Response:
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            Order.objects.get(
                product=serializer.validated_data['product'],
                customer=request.user)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.validated_data['customer'] = request.user
        serializer.save()
        return Response(status=status.HTTP_200_OK)
