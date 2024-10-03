from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey
from rest_framework.exceptions import Throttled

from .models import ScrapedData
from .serializers import ScrapedDataSerializer
from .tasks import extract_emails
from .throttling import ConcurrencyThrottleApiKey

class ScrapedDataViewSet(viewsets.ModelViewSet):
    serializer_class = ScrapedDataSerializer

    def get_queryset(self):
        # Extract the API key from the Authorization header
        auth_header = self.request.headers.get("Authorization")
        if auth_header is None or " " not in auth_header:
            return ScrapedData.objects.none()
        api_key = auth_header.split(" ")[1]
        username = APIKey.objects.get_from_key(api_key).name
        user = User.objects.get(username=username)
        return ScrapedData.objects.filter(user=user)

    def get_throttle_classes(self):
        if self.action == "create":
            return [ConcurrencyThrottleApiKey]
        return []

    def create(self, request, *args, **kwargs):
        # Apply the custom throttle
        throttle = ConcurrencyThrottleApiKey()
        if not throttle.allow_request(request, self):
            raise Throttled(detail="Rate limit exceeded. Please try again later.")

        # Get the user object
        auth_header = request.headers.get("Authorization")
        if auth_header is None or " " not in auth_header:
            return Response({"detail": "Invalid Authorization header"}, status=status.HTTP_400_BAD_REQUEST)
        api_key = auth_header.split(" ")[1]
        username = APIKey.objects.get_from_key(api_key).name
        user = User.objects.get(username=username)

        # Validate and save the scraped data
        serializer = ScrapedDataSerializer(data=request.data)
        if serializer.is_valid():
            scraped_data = serializer.save(
                user=user,  # Save the user information
                status=ScrapedData.Status.PENDING,
            )
            # Call the Celery task
            extract_emails.delay(scraped_data.link, scraped_data.id)
            return Response(
                {
                    "id": scraped_data.id,
                    "message": "Scraped data has been submitted successfully",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)