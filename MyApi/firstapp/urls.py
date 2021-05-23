from django.db import router
from django.urls import path, include
from .views import first_function, CarSpecsViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('car-specs', CarSpecsViewset, basename="car-specs")


urlpatterns = [
    path('first/', first_function, name="home-page"),
    path('', include(router.urls))
]
