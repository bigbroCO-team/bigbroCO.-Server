from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('name', 'zipcode', 'address', 'detail', 'phone', 'request')
