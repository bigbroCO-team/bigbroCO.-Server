# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from order.serializers import CreateOrderListSerializer


class CreateOrderListView(APIView):
    def post(self, request: object) -> Response:
        serializer = CreateOrderListSerializer


        return Response(status=status.HTTP_201_CREATED)
