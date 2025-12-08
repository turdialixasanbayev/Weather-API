from rest_framework import serializers

from apps.weather.models import Village


class VillageUpdateAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = Village
        fields = ['name', 'district']
