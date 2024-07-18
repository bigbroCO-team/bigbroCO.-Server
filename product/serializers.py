from rest_framework import serializers

from product.models import Image, Product

from option.serializers import OptionSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
