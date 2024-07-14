import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import User


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'signature', 'phone')

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        if password is None:
            return ValidationError('Password is required.')

        if not re.match(r'^010([0-9]{4})([0-9]{4})$', validated_data.get('phone')):
            raise ValidationError('Phone number is invalid')

        return User.objects.create_user(
            **validated_data,
            password=password
        )
