from django.urls import path

from .api.Country.CountryList.views import CountryListAPIView
from .api.Country.CountryDetail.views import CountryRetrieveAPIView
from .api.Country.CountryCreate.views import CountryCreateAPIView
from .api.Country.CountryDelete.views import CountryDeleteAPIView
from .api.Country.CountryUpdate.views import CountryUpdateAPIView

from .api.Region.RegionList.views import RegionListAPIView
from .api.Region.RegionDelete.views import as_view
from .api.Region.RegionRetrieve.views import RegionDetailAPIView
from .api.Region.RegionUpdate.views import RegionUpdateAPIView
from apps.weather.api.Region.RegionCreate.views import RegionCreateAPIView


urlpatterns = [
    path(
        'country-list/',
        CountryListAPIView.as_view(),
        name='country-list',
    ),
    path(
        'country-create/',
        CountryCreateAPIView.as_view(),
        name='country-create',
    ),
    path(
        'country-detail/<int:pk>/',
        CountryRetrieveAPIView.as_view(),
        name='country-detail',
    ),
    path(
        'country-delete/<int:pk>/',
        CountryDeleteAPIView.as_view(),
        name='country-delete',
    ),
    path(
        'country-update/<int:pk>/',
        CountryUpdateAPIView.as_view(),
        name='country-update',
    ),
    path(
        'region-list/',
        RegionListAPIView.as_view(),
        name='region-list',
    ),
    path(
        'region-delete/<int:pk>/',
        as_view,
        name='region-delete',
    ),
    path(
        'region-detail/<int:pk>/',
        RegionDetailAPIView.as_view(),
        name='region-detail',
    ),
    path(
        'region-update/<int:pk>/',
        RegionUpdateAPIView.as_view(),
        name='region-update',
    ),
    path(
        'region-create/',
        RegionCreateAPIView.as_view(),
        name='region-create',
    ),
]
