from rest_framework import serializers

from apps.weather.models import Region
from apps.weather.api.Country.CountryList.serializers import CountryListAPISerializer


class RegionListAPISerializer(serializers.ModelSerializer):
    country = CountryListAPISerializer(read_only=True)

    class Meta:
        model = Region
        fields = ['name', 'country']
