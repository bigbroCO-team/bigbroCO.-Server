import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.auth.func import IsAuthenticated
from .models import Address
from config.settings import SECRET_KEY
from .serializers import AddressSerializer
from common.models import Customer


# Create your views here.
class AddressView(APIView):
    @IsAuthenticated
    def get(self, request: object) -> Response:
        token = request.COOKIES.get('access')
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        username = payload.get('username')
        user = Customer.objects.filter(username=username).first()

        address = Address.objects.filter(customer=user).first()
        serializer = AddressSerializer(instance=address)
        return Response(serializer.data)

    @IsAuthenticated
    def post(self, request: object) -> Response:
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = request.COOKIES.get('access')
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        user = Customer.objects.filter(username=payload.get('username')).first()
        serializer.validated_data['customer'] = user

        serializer.save()

        return Response(serializer.data)
