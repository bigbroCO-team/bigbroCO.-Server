from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'name', 'zipcode', 'address', 'detail', 'request')

        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': True},
            'zipcode': {'required': True},
            'address': {'required': True},
            'detail': {'required': True},
            'request': {'required': False}}
