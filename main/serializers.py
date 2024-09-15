from .models import ScrapedData
from rest_framework import serializers


class ScrapedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedData
        fields = ['id', 'title', 'link', 'description']
        read_only_fields = ['description']