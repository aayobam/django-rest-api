from django.urls import path
from django.urls.conf import include
from .views import PostViewSet, PostRateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("post-list", PostViewSet, basename="post-list")
router.register("post-rate", PostRateViewSet, basename="post-rate")


urlpatterns = [
    path('', include(router.urls)),
]
