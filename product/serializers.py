from rest_framework import serializers

from product.models import Product, Category, Size


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    size = SizeSerializer(source='size.name', read_only=True)
    category = CategorySerializer(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

