from django.contrib import admin
from .models import ScrapedData

# Register your models here.
@admin.register(ScrapedData)
class ScrapedDataAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'status', 'created_at']
    search_fields = ['title', 'link', 'data']
    list_filter = ['created_at', 'updated_at', "status"]
    list_per_page = 10
