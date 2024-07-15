from rest_framework import serializers

from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

        extra_kwargs = {
            'id': {'required': False},
            'user': {'required': False}
        }
