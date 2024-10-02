from rest_framework import serializers

from src.app.client.cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartSerializerWithoutUser(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'product', 'option', 'count')

    def create(self, validated_data):
        user = validated_data.pop('user', None)
        origin_cart = Cart.objects.filter(
            user=user,
            product=validated_data.get('product'),
            option=validated_data.get('option')
        ).first()

        if origin_cart:
            origin_cart.count += 1
            origin_cart.save()
            return origin_cart
        else:
            return Cart.objects.create(**validated_data)
