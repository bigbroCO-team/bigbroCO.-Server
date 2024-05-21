from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Address
from .serializers import AddressSerializer
from common.models import Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class AddressView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: object) -> Response:
        address = Address.objects.filter(customer=request.user)
        serializer = AddressSerializer(instance=address, many=True)
        return Response(serializer.data)

    def post(self, request: object) -> Response:
        user = Customer.objects.get(username=request.user)

        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['customer'] = user
        serializer.save()

        return Response(serializer.data)
