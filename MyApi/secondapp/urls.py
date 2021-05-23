from django.urls import path
from .views import CarsApiView


urlpatterns = [
    path('second/', CarsApiView.as_view(), name="second-app"),
]
