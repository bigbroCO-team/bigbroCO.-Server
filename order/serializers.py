from rest_framework import serializers

from order.models import ProductItem, Order
from product.models import Product, Option


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = ProductItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'delivery', 'tracking_number', 'total', 'address', 'address_detail', 'zipcode', 'request']

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)

        return order
