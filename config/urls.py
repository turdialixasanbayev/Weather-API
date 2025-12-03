from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from config import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Weather API",
      default_version='v1',
      description="Weather API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="turdialixasanbayev@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAdminUser,),
)


urlpatterns = [
    path(
        'weather-admin-panel/',
        admin.site.urls,
    ),

    path(
        'api/weather/',
        include('apps.weather.urls')
    ),
    path(
        'api/user/',
        include('apps.user.urls')
    ),

    path('swagger/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    re_path(
        r'^mediafiles/(?P<path>.*)$',
        serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
    re_path(
        r'^staticfiles/(?P<path>.*)$',
        serve,
        {'document_root': settings.STATIC_ROOT},
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
