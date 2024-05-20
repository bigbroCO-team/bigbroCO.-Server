from rest_framework import status
from rest_framework.exceptions import ValidationError
from .serializers import SignupSerializer
from config import settings
from .models import Image
from config.settings import AWS_STORAGE_BUCKET_NAME, AWS_S3_INSTANCE_URL
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from uuid import uuid4
import re
import os


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


class UploadView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request: object) -> Response:
        image = request.FILES.get('image', None)
        if not image:
            raise ValidationError('Image is required')

        name, extension = os.path.splitext(image.name)
        if extension.lower() not in ['.jpg', '.jpeg', '.png']:
            raise ValidationError('Image must be JPEG or PNG')

        path = f'{str(uuid4())}{extension}'
        save = default_storage.save(os.path.join(settings.MEDIA_ROOT, path), image)
        s3path = f'https://{AWS_S3_INSTANCE_URL}/{AWS_STORAGE_BUCKET_NAME}/{save}'

        Image.objects.create(url=s3path)

        return Response({'path': s3path}, status=status.HTTP_201_CREATED)
