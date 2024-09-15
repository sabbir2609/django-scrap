from django.db import models


class ScrapedData(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    description = models.TextField(
        blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Scraped Data'
        ordering = ['-created_at']
