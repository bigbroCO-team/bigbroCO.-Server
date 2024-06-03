from rest_framework import serializers
from common.models import Image
from product.models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

        extra_kwargs = {
            'id': {'required': False},
            'product': {'required': False},
        }


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

        extra_kwargs = {
            'seller': {'required': False},
        }

    def create(self, validated_data):
        image = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        for i in image:
            ProductImage.objects.create(product=product, **i)
        return product
