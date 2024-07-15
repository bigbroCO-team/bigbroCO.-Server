from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from address.models import Address
from address.serializers import AddressSerializer
from user.models import User


# Create your views here.
class AddressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: object) -> Response:
        return Response(
            AddressSerializer(
                Address.objects.filter(user=request.user),
                many=True
            ).data,
            status=status.HTTP_200_OK
        )

    def post(self, request: object) -> Response:
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=User.objects.get(id=request.user.id)
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, id: int) -> Response:
        serializer = AddressSerializer(
            instance=Address.objects.get(id=id, user=request.user),
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: object, id: int) -> Response:
        Address.objects.get(id=id, user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)