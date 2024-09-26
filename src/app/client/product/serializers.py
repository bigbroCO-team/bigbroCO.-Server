from rest_framework import serializers

from src.app.client.product.models import Product, Image, Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

        extra_kwargs = {
            'product': {'required': False},
        }


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

        extra_kwargs = {
            'product': {'required': False},
        }


class ProductSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
