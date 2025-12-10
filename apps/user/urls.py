from django.urls import path

from apps.user.views.me import MeAPIView
from apps.user.views.set_village import UserSetVillageAPIView
from apps.user.views.get_weather import GetWeatherAPIView
from apps.user.views.get_full_location import UserLocationAPIView
from apps.user.views.get_country import GetCountryAPIView
from apps.user.views.get_village import GetVillageAPIView

from apps.user.views.get_region_and_get_district import (
    GetDistrictAPIView,
    GetRegionAPIView,
)

from ..user.views.search_village import SearchVillageAPIView

### Auth urls

from apps.user.api.Register.views import RegisterView
from apps.user.api.Login.views import LoginView
from apps.user.api.Refresh.views import CustomTokenRefreshView
from apps.user.api.Verify.views import CustomTokenVerifyView


urlpatterns = [
    path(
        'me/',
        MeAPIView.as_view(),
        name='me',
    ),
    path(
        'set-village/',
        UserSetVillageAPIView.as_view(),
        name='set-village',
    ),
    path(
        'get-village/',
        GetVillageAPIView.as_view(),
        name='get-village',
    ),
    path(
        'get-weather/',
        GetWeatherAPIView.as_view(),
        name='get-weather',
    ),
    path(
        'get-full-location/',
        UserLocationAPIView.as_view(),
        name='get-full-location',
    ),
    path(
        'get-country/',
        GetCountryAPIView.as_view(),
        name='get-country',
    ),
    path(
        'get-region/',
        GetRegionAPIView.as_view(),
        name='get-region',
    ),
    path(
        'get-district/',
        GetDistrictAPIView.as_view(),
        name='get-district',
    ),
    path(
        'search-village/',
        SearchVillageAPIView.as_view(),
        name='search-village',
    ),

    ### Auth urls
    path(
        'register/',
        RegisterView.as_view(),
        name='register',
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='login',
    ),
    path(
        'token/refresh/',
        CustomTokenRefreshView.as_view(),
        name='token_refresh',
    ),
    path(
        'token/verify/',
        CustomTokenVerifyView.as_view(),
        name='token_verify',
    ),
]
