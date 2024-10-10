from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.test import APIClient

from product.models import Product, Option
from account.models import User


class CartTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            category='CBWAS',
            name='CBWAS',
            description='CBWAS',
            price=10000,
            discount=0
        )
        self.option = Option.objects.create(
            product = self.product,
            name='test'
        )
        self.user = User.objects.create(
            email='test@test.com',
        )
        token = TokenObtainPairSerializer.get_token(self.user)
        self.access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_get_cart(self):
        path = reverse('cart')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

    def test_create_cart(self):
        path = reverse('cart')
        data = {
            'product': self.product.id,
            'option': self.option.id,
            'count': 1,
        }
        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, 201)
