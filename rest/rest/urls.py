
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Contact List API",
      default_version='v1',
      description="An api for contacts",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@contacts.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/auth/', include('authentication.urls')),
    path('apis/contacts/', include('contacts.urls')),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('accounts.urls')),
]
