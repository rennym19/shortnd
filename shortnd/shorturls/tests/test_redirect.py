from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ..models import URL
from ..key_generator import gen_key

class RedirectTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.view_name = 'shortnd:redirect'
        url = URL(original_url='https://www.github.com', title='GitHub', key=gen_key(url_id=1))
        url.save()
        self.key = url.key

    def test_redirect_url(self):
        response = self.client.get(reverse(self.view_name, kwargs={'key': self.key}))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_redirect_invalid_url(self):
        response = self.client.get(reverse(self.view_name, kwargs={'key': 'F0eQac'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {
            'error': 'URL Not Found'
        })
