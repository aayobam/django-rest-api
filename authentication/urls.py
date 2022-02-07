from .views import *
from django.urls import path
from .views import AuthUserApiview



urlpatterns = [
    path('register', RegisterApiView.as_view(), name="register"),
    path('login', LoginApiView.as_view(), name="login"),
    path('user', AuthUserApiview.as_view(), name="user")
]
