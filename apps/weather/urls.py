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
from .api.Region.RegionCreate.views import RegionCreateAPIView

from .api.District.DistrictCreate.views import DistrictCreateAPIView
from .api.District.DistrictUpdate.views import DistrictUpdateAPIView
from .api.District.DistrictList.views import DistrictListAPIView
from .api.District.DistrictRetrieve.views import DistrictRetrieveAPIView
from .api.District.DistrictDestroy.views import DistrictDestroyAPIView

from .api.Village.VillageList.views import VillageListAPIView
from .api.Village.VillageRetrieve.views import VillageDetailAPIView
from .api.Village.VillageDestroy.views import VillageDeleteAPIView
from .api.Village.VillageUpdate.views import VillageUpdateAPIView
from .api.Village.VillageCreate.views import VillageCreateAPIView


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
    path(
        'district-create/',
        DistrictCreateAPIView.as_view(),
        name='district-create',
    ),
    path(
        'district-update/<int:pk>/',
        DistrictUpdateAPIView.as_view(),
        name='district-update',
    ),
    path(
        'district-list/',
        DistrictListAPIView.as_view(),
        name='district-list',
    ),
    path(
        'district-retrieve/<int:pk>/',
        DistrictRetrieveAPIView.as_view(),
        name='district-retrieve',
    ),
    path(
        'district-destroy/<int:pk>/',
        DistrictDestroyAPIView.as_view(),
        name='district-destroy',
    ),
    path(
        'village-list/',
        VillageListAPIView.as_view(),
        name='village-list',
    ),
    path(
        'village-detail/<int:pk>/',
        VillageDetailAPIView.as_view(),
        name='village-detail',
    ),
    path(
        'village-delete/<int:pk>/',
        VillageDeleteAPIView.as_view(),
        name='village-delete',
    ),
    path(
        'village-update/<int:pk>/',
        VillageUpdateAPIView.as_view(),
        name='village-update',
    ),
    path(
        'village-create/',
        VillageCreateAPIView.as_view(),
        name='village-create',
    ),
]
