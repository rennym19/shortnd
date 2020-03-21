from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views import View
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.db.models import ObjectDoesNotExist

from .serializers import URLSerializer
from .models import URL

class Index(View):
    def get(self, request):
        return HttpResponse('Hello')


class Shortener(APIView):
    def post(self, request):
        original_url = request.data['url'] if 'url' in request.data else None
        if original_url is None:
            return Response({'error': 'URL needed'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = URLSerializer(data={'original_url': original_url})
        
        if serializer.is_valid():
            url = serializer.create(serializer.validated_data)
            url.fetch_title()
            return Response(URLSerializer(url).data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid URL'}, status=status.HTTP_400_BAD_REQUEST)


class Redirect(APIView):
    def get_url(self, key):
        try:
            return URL.objects.get(key=key)
        except ObjectDoesNotExist:
            return None

    def get(self, request, key):
        url = self.get_url(key)
        if url is not None:
            return HttpResponseRedirect(url.original_url)
        return Response({'error': 'URL Not Found'}, status=status.HTTP_404_NOT_FOUND)


class TopHundred(APIView):
    def get(self, request):
        urls = URL.top_hundred.all()
        serializer = URLSerializer(urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)