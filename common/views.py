import datetime
import jwt
from .serializers import CustomerSerializer, AddressSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Address
from rest_framework.exceptions import AuthenticationFailed
from config.settings import SECRET_KEY
from utils.auth.func import IsAuthenticated


# Create your views here.
class SignupView(APIView):
    def post(self, request: object) -> Response:
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request: object) -> Response:
        username = request.data['username']
        password = request.data['password']

        user = Customer.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('Login fail')

        if not user.check_password(password):
            raise AuthenticationFailed('Login fail')

        payload = {
            'username': user.username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=3),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        response = Response()
        response.set_cookie(key='token', value=token, httponly=True)

        return response


class LogoutView(APIView):
    def delete(self, request: object) -> Response:
        response = Response()
        response.delete_cookie(key='token')
        return response


class AddressView(APIView):
    @IsAuthenticated
    def get(self, request: object) -> Response:
        token = request.COOKIES.get('token')
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

        token = request.COOKIES.get('token')
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        user = Customer.objects.filter(username=payload.get('username')).first()
        serializer.validated_data['customer'] = user

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)