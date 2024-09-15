from rest_framework import viewsets
from .models import ScrapedData
from .serializers import ScrapedDataSerializer
# from .tasks import scraped_data
from rest_framework.response import Response
from rest_framework import status


class ScrapedDataViewSet(viewsets.ModelViewSet):
    queryset = ScrapedData.objects.all()
    serializer_class = ScrapedDataSerializer
