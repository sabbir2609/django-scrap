from .models import ScrapedData
from rest_framework import serializers


class ScrapedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedData
        fields = ["id", "title", "link", "data", "status", "created_at"]
        read_only_fields = ["id", "user", "data", "status", "created_at"]
