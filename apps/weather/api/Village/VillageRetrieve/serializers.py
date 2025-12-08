from rest_framework import serializers

from apps.weather.models import Village
from apps.weather.api.District.DistrictRetrieve.serializers import DistrictRetrieveAPISerializer


class VillageDetailAPISerializer(serializers.ModelSerializer):
    district = DistrictRetrieveAPISerializer(read_only=True)

    class Meta:
        model = Village
        fields = ['name', 'district']
