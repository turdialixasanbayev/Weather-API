from rest_framework import serializers

from apps.weather.models import Village


class VillageCreateAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = Village
        fields = ['name', 'district']

    def create(self, validated_data):
        village = Village.objects.create(**validated_data)
        return village
