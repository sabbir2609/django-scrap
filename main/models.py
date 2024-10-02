import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ScrapedData(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        SUCCESS = "SUCCESS", "Success"
        FAILED = "FAILED", "Failed"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_("Unique identifier for the scraped data"),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text=_("User who initiated the scraping")
    )
    title = models.CharField(max_length=100, help_text=_("Title of the scraped data"))
    link = models.URLField(
        max_length=200, help_text=_("URL from which the data was scraped")
    )
    data = models.TextField(
        blank=True, null=True, help_text=_("The actual scraped data")
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        help_text=_("Current status of the scraping process"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True, help_text=_("Timestamp when the data was created")
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text=_("Timestamp when the data was last updated")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Scraped Data"
        ordering = ["-created_at"]
