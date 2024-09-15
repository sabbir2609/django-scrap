from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegistrationSerializer, UserMeSerializer


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        # Validate and save the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Ensure the user is saved first

        # Generate an API key and associate it with the user
        api_key, key = APIKey.objects.create_key(name=user.username)

        return Response(
            {"username": user.username, "api_key": key}, status=status.HTTP_201_CREATED
        )


# This viewset is used to retrieve the user's own information using their API key
class UserMeViewSet(viewsets.ModelViewSet):
    serializer_class = UserMeSerializer
    permission_classes = [HasAPIKey]

    # Get the queryset for the authenticated user based on the API key
    def get_queryset(self):
        # Extract the API key from the Authorization header
        api_key = self.request.headers.get("Authorization").split(" ")[1]
        user = APIKey.objects.get_from_key(api_key).name
        # Return the user object
        return User.objects.filter(username=user)
    
    def patch(self, request, *args, **kwargs):
        # Get the user object
        user = self.get_queryset().first()
        # Validate and save the user
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
