from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.shortcuts import HttpResponseRedirect
from django.db.models import ObjectDoesNotExist

from .pagination import BasicPagination, PaginationHandlerMixin, paginate_serializer
from .serializers import URLSerializer
from .models import URL


index = never_cache(TemplateView.as_view(template_name='frontend/index.html'))


class Shortener(APIView):
    def post(self, request):
        original_url = request.data['url'] if request.data and 'url' in request.data else None
        if original_url is None:
            return Response({'error': 'URL needed'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = self.get_url_if_already_shortened(original_url)
        if url is not None:
            url.fetch_title_if_not_set()
            return Response(URLSerializer(url).data, status=status.HTTP_200_OK)

        serializer = URLSerializer(data={'original_url': original_url}, context={'request': request})
        if serializer.is_valid():
            url = serializer.create(serializer.validated_data)
            return Response(URLSerializer(url).data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid URL'}, status=status.HTTP_400_BAD_REQUEST)

    def get_url_if_already_shortened(self, original_url):
        try:
            return URL.objects.get(original_url=original_url)
        except ObjectDoesNotExist:
            return None


class Redirect(APIView):
    def get_url(self, key):
        try:
            return URL.objects.get(key=key)
        except ObjectDoesNotExist:
            return None

    def get(self, request, key):
        url = self.get_url(key)
        if url is not None:
            url.visit_count += 1
            url.save()
            url.fetch_title_if_not_set()
            return HttpResponseRedirect(url.original_url)
        return Response({'error': 'URL Not Found'}, status=status.HTTP_404_NOT_FOUND)


class TopHundred(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request):
        urls = URL.top_hundred.all()
        serializer = paginate_serializer(self, URLSerializer, urls)
        return Response(serializer.data, status=status.HTTP_200_OK)
