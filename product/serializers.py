from rest_framework import serializers

from option.models import Option
from product.models import Image, Product

from option.serializers import OptionSerializer


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

    def create(self, validated_data):
        options = validated_data.pop('options')
        images = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        for option in options:
            Option.objects.create(product=product, **option)
        for image in images:
            Image.objects.create(product=product, **image)
        return product
