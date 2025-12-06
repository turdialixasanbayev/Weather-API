from rest_framework import serializers

from apps.weather.models import District


class DistrictUpdateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name', 'region']
