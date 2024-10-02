from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey
from django.contrib.auth.models import User
from .models import ScrapedData
from .serializers import ScrapedDataSerializer
from .tasks import extract_emails


class ScrapedDataViewSet(viewsets.ModelViewSet):
    serializer_class = ScrapedDataSerializer

    def get_queryset(self):
        # Extract the API key from the Authorization header
        api_key = self.request.headers.get("Authorization").split(" ")[1]
        username = APIKey.objects.get_from_key(api_key).name
        user = User.objects.get(username=username)
        return ScrapedData.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        # Get the user object
        api_key = self.request.headers.get("Authorization").split(" ")[1]
        username = APIKey.objects.get_from_key(api_key).name
        user = User.objects.get(username=username)
        # Validate and save the scraped
        serializer = ScrapedDataSerializer(data=request.data)
        if serializer.is_valid():
            scraped_data = serializer.save(
                user=user,  # Save the user information
                status=ScrapedData.Status.PENDING,
            )
            # Call the Celery task
            extract_emails.delay(scraped_data.link, scraped_data.id)
            return Response(
                f"Scraped data with id {scraped_data.id} has been created and it's processing, please check back later",
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
