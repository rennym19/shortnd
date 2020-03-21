from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ..models import URL

class ShortenTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('shortnd:shorten')

    def test_shorten_invalid_url(self):
        invalid_data = {'url': 'dasdas'}
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(URL.objects.count(), 0)
        self.assertEqual(response.data, {
            'error': 'Invalid URL'
        })
    
    def test_shorten_no_url(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(URL.objects.count(), 0)
        self.assertEqual(response.data, {
            'error': 'URL needed'
        })
    
    def test_shorten_url(self):
        data = {'url': 'https://www.google.com'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = URL.objects.get()
        self.assertEqual(response.data, {
            'id': url.pk, 
            'original_url': url.original_url, 
            'key': url.key,
            'short_url': url.short_url,
            'visit_count': url.visit_count
        })

    def test_shorten_already_shortened_url(self):
        data = {'url': 'https://www.amazon.com/'}
        response = self.client.post(self.url, data, format='json')
        url = URL.objects.order_by('-id').first()
        num_urls = URL.objects.count()

        new_response = self.client.post(self.url, data, format='json')
        new_url = URL.objects.order_by('-id').first()
        new_num_urls = URL.objects.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(url.short_url, new_url.short_url)
        self.assertEqual(num_urls, new_num_urls)
        