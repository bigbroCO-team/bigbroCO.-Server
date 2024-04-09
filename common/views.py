from .serilizers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from others.Jwt.JwtHandler import JwtHandler
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


# Create your views here.
class SignupView(APIView):
    def post(self, request: object) -> Response:
        request.data['password'] = make_password(request.data.get('password'))
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if user is not None:
            return JwtHandler.setToken(user=user)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def delete(self, request: object) -> Response:
        return JwtHandler.deleteToken()
