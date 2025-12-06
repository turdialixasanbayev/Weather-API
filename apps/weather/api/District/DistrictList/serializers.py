from rest_framework import serializers

from apps.weather.models import District
from apps.weather.api.Region.RegionList.serializers import RegionListAPISerializer


class DistrictListAPISerializer(serializers.ModelSerializer):
    region = RegionListAPISerializer(read_only=True)
    class Meta:
        model = District
        fields = ['name', 'region']
