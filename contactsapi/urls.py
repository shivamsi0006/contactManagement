from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Contacts API",
      default_version='v1',
      description="API for managing contacts and authentication",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentictaion.urls')),
    path('api/contacts/', include('contacts.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI route
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
