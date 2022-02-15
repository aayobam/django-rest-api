from .views import *
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('register', RegisterUserApiView.as_view(), name="register"),
    path('login', MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('all', LoggedInUsersView.as_view(), name="logged_in_users"),
    path("<uuid:user_id>", UserAPIView.as_view(), name="user"),
    path('logout', LogOutApiView.as_view(), name="logout"),  
]
