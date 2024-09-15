from rest_framework.routers import DefaultRouter

from .views import ScrapedDataViewSet


app_name = 'main'


router = DefaultRouter()
router.register(r'scraped_data', ScrapedDataViewSet, basename='scraped_data')

urlpatterns = router.urls