from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from thirdparty.s3 import s3


class UploadView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        image = request.FILES.get('file', None)
        url = s3.upload(image)
        return Response({'url': url}, status=status.HTTP_201_CREATED)
