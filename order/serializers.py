from rest_framework import serializers

from address.models import Address
from order.models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

        extra_kwargs = {
            'order': {'required': False},
        }


class CreateOrderListSerializer(serializers.Serializer):
    products = OrderItemSerializer(many=True)
    request = serializers.CharField()
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())

    def create(self, validated_data):
        user = validated_data.pop('user')
        address = validated_data.pop('address')
        products = validated_data.pop('products')
        name = f"{products[0]['product'].name} {products[0]['option'].name}{f' 외 {len(products) - 1} 개' if len(products) > 1 else ''}"
        amount = 0
        for p in products:
            amount += int(p['product'].price / (int(100 - p['product'].discount) / 100))

        order = Order.objects.create(
            name=name,
            user=user,
            address=address.address,
            address_detail=address.detail,
            zipcode=address.zipcode,
            request=validated_data['request'],
            total=amount
        )

        for p in products:
            OrderItem.objects.create(
                order=order,
                product=p['product'],
                option=p['option']
            )

        return order
