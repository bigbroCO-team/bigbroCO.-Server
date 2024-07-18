from rest_framework import serializers

from option.models import Option
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

    def create(self, validated_data):
        options = validated_data.pop('options')
        product = Product.objects.create(**validated_data)
        Option.objects.create(product=product, **options)
        return product
