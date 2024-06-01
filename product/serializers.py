from rest_framework import serializers

from product.models import Product, Rating


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': True},
            'price': {'required': True},
            'description': {'required': True},
            'size': {'required': True},
            'category': {'required': True},
            'date': {'required': True},
            'onsale': {'required': False},
            'discount': {'required': False},
        }


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('value', 'product')
