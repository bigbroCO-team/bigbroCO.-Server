from .serilizers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


# Create your views here.
class SignupView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return JWToken.SetToken(user=user)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if user is not None:
            return JWToken.SetToken(user=user)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def delete(self, request):
        return JWToken.DeleteToken()


class JWToken():
    def SetToken(user):
        res = Response({}, status=status.HTTP_200_OK)
        token = TokenObtainPairSerializer.get_token(user)
        refreshToken = str(token)
        accessToken = str(token.access_token)
        res = Response({}, status=status.HTTP_200_OK)
        res.set_cookie("accessToken", accessToken, httponly=True)
        res.set_cookie("refreshToken", refreshToken, httponly=True)
        return res

    def DeleteToken(self):
        res = Response({}, status=status.HTTP_202_ACCEPTED)
        res.delete_cookie("accessToken")
        res.delete_cookie("refreshToken")
        return res