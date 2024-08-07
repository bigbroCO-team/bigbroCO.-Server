from rest_framework import serializers

from cart.models import Cart
from product.serializers import ProductSerializer, OptionSerializer


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    option = OptionSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

        extra_kwargs = {
            'id': {'required': False},
            'user': {
                'required': False,
                'write_only': True
            },
        }
