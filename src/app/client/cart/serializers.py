from rest_framework import serializers

from src.app.client.cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

        extra_kwargs = {
            'user': {'required': False},
        }

    def create(self, validated_data):
        exists_cart = Cart.objects.filter(user=validated_data.get('user'))
        for i, cart in enumerate(exists_cart):
            if validated_data.get(i) == cart:  # 기존 상품이 존재
                cart.count += 1
            else:
                exists_cart.add(validated_data.get(i))
        exists_cart.save()
        return exists_cart