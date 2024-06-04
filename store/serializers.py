from rest_framework import serializers

from store.models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

        extra_kwargs = {
            'customer': {'required': False},
        }
