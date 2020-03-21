from rest_framework import serializers
import re

from .models import URL
from .key_generator import gen_key


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['id', 'original_url', 'key', 'short_url', 'title', 'visit_count']
        read_only_fields = ['id', 'visit_count', 'short_url', 'title', 'key']

    def __init__(self, instance=None, data=serializers.empty, **kwargs):
        super().__init__(instance, data, **kwargs)

    def validate_original_url(self, val):
        URL_PATTERN = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
        is_valid_url = re.match(URL_PATTERN, val)

        if not is_valid_url:
            raise serializers.ValidationError('Invalid URL')

        return val

    def create(self, validated_data):
        if 'request' not in self.context or self.context.get('request') is None:
            raise serializers.ValidationError('Request needed')
        http_request = self.context.get('request')

        url = URL(**validated_data)
        url.save()
        url.key = gen_key(url.pk)
        url.short_url = '{0}://{1}/{2}'.format(
            http_request.scheme, http_request.get_host(), url.key
        )
        url.save()
        url.fetch_title_if_not_set()
        return url
