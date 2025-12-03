from django.urls import path

from .api.Country.CountryList.views import CountryListAPIView
from .api.Country.CountryDetail.views import CountryRetrieveAPIView
from .api.Country.CountryCreate.views import CountryCreateAPIView
from .api.Country.CountryDelete.views import CountryDeleteAPIView
from .api.Country.CountryUpdate.views import CountryUpdateAPIView

from .api.Region.RegionList.views import RegionListAPIView


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
]
