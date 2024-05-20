from .models import Customer
from rest_framework import serializers



class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'password', 'email', 'last_name', 'phone')

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data.pop('validate', None)
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance