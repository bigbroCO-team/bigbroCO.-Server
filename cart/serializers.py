from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

        extra_kwargs = {
            'id': {'required': False},
            'user': {'required': False},
        }