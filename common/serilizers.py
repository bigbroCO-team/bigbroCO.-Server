from .models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        user = Customer.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        return user
