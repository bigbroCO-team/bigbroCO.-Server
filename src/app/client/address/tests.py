from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from src.app.client.user.models import User


class AddressTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.com',
        )
        token = TokenObtainPairSerializer.get_token(self.user)
        self.access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_get_address(self):
        path = reverse('address')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_address(self):
        path = reverse('address')
        data = {
            'tag': 'test',
            'name': 'test',
            'zipcode': '123123',
            'phone': '01012341234',
            'address': 'test',
            'detail': 'test'
        }
        response = self.client.post(path, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)