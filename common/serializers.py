from .models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

