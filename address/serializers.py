from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': True},
            'zipcode': {'required': True},
            'address': {'required': True},
            'detail': {'required': True},
            'request': {'required': False}}
