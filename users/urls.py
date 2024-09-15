from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet, UserMeViewSet


app_name = "users"


router = DefaultRouter()

router.register("register", UserRegistrationViewSet, basename="register")
router.register("me", UserMeViewSet, basename="user-me")

urlpatterns = router.urls