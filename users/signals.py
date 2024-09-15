from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework_api_key.models import APIKey

@receiver(post_delete, sender=User)
def delete_user_api_key(sender, instance, **kwargs):
    try:
        user_api_key = APIKey.objects.get(name=instance.username)
        user_api_key.delete()
    except APIKey.DoesNotExist:
        pass  # If the UserAPIKey does not exist, do nothing