from rest_framework import serializers

from apps.weather.models import Country


class CountryListAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'code']
