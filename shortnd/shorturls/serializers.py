from rest_framework import serializers
from .models import URL
from .key_generator import gen_key

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['id', 'original_url', 'key', 'short_url', 'title', 'visit_count']
        read_only_fields = ['id', 'visit_count', 'short_url', 'key']

    def validate_original_url(self, val):
        return val

    def create(self, validated_data):
        url = URL(**validated_data)
        url.save()

        url.key = gen_key(url.pk)
        return url
