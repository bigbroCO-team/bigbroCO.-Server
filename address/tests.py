from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from address.models import Address
from user.models import User


# Create your tests here.
class UploadAddressTestCode(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test')
        self.client.force_authenticate(self.user)
        self.address = Address.objects.create(
            user=self.user,
            tag="test",
            zipcode="12345",
            phone="01012341234",
            address="test",
            detail="test",
            request="test"
        )

    def test_get_address(self):
        r = self.client.get('/address')
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_post_address(self):
        r = self.client.post('/address', data={
            'tag': 'test1234',
            'zipcode': '12345',
            'phone': '01012341234',
            'address': 'test',
            'detail': 'test',
            'request': 'test'
        }, format='json')
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

    def test_put_address(self):
        r = self.client.put(f'/address/{self.address.id}', data={
            'tag': 'test12341',
            'zipcode': '12345',
            'phone': '01012341234',
            'address': 'test',
            'detail': 'test',
            'request': 'test'
        }, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_delete_address(self):
        r = self.client.delete(f'/address/{self.address.id}')
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
