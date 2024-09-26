from rest_framework import serializers

from src.app.client.address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

        extra_kwargs = {
            'user': {'required': False},
        }

    def create(self, validated_data):
        return Address.objects.create(**validated_data)
