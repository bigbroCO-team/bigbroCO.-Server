from rest_framework import serializers
from shopping.models import Wishlist, Cart


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

        extra_kwargs = {
            'customer': {'required': False},
        }


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

        extra_kwargs = {
            'customer': {'required': False},
        }
