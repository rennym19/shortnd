from rest_framework import serializers
import re

from .models import URL
from .key_generator import gen_key

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['id', 'original_url', 'key', 'short_url', 'title', 'visit_count']
        read_only_fields = ['id', 'visit_count', 'short_url', 'title', 'key']

    def validate_original_url(self, val):
        URL_PATTERN = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
        is_valid_url = re.match(URL_PATTERN, val)

        if not is_valid_url:
            raise serializers.ValidationError('Invalid URL')

        return val

    def create(self, validated_data):
        url = URL(**validated_data)
        url.save()
        url.key = gen_key(url.pk)
        url.save()
        return url
