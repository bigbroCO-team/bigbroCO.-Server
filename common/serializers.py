from .models import Customer, Image
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'password', 'email', 'phone')

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'phone': {'required': True},
        }

    def create(self, validated_data):
        validated_data.pop('validate', None)
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

        def get_photo_url(self, obj):
            request = self.context.get('request')
            photo_url = obj.fingerprint.url
            return request.build_absolute_uri(photo_url)
