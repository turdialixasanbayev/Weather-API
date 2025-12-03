from rest_framework import serializers

from apps.weather.models import Country


class CountryCreateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'code']
