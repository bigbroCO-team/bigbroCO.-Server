import datetime
import jwt
from .serializers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from rest_framework.exceptions import AuthenticationFailed
from config.settings import SECRET_KEY


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