from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view



schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="Todo web app documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[]
)
urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/v1/users/', include('apps.authentication.urls')),
   path('api/v1/todo/', include('apps.todos.urls')),

   # drf-yasg open api
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

admin.site.site_title = "Todo Admin"
admin.site.site_header ="Todo Administrator"