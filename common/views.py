from .serializers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class SignupView(APIView):
    def post(self, request: object) -> Response:
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
