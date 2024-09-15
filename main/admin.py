from django.contrib import admin
from .models import ScrapedData

# Register your models here.
@admin.register(ScrapedData)
class ScrapedDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'link', 'description', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'link', 'description']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10
