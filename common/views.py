from rest_framework import status
from rest_framework.exceptions import ValidationError
from .serializers import SignupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import re



# Create your views here.
class SignupView(APIView):
    def post(self, request: object) -> Response:
        validate = request.data.pop('validate', None)
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        if not re.match(r'^010([0-9]{4})([0-9]{4})$', validated_data['phone']):
            raise ValidationError('Phone number is invalid')

        if validated_data['password'] != validate:
            raise ValidationError('Passwords do not match')

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)