from rest_framework import serializers

from src.app.address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

        extra_kwargs = {
            'user': {
                'required': False,
                'write_only': True
            },
        }
