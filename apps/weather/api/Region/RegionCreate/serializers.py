from rest_framework import serializers

from apps.weather.models import Region


class RegionCreateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name', 'country']
