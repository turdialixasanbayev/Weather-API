from rest_framework import serializers

from apps.weather.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    """
    This serializer handles the serialization and deserialization of Weather model instances.
    """

    class Meta:
        model = Weather
        exclude = ['id', 'updated_at']

        def create(self, validated_data):
            return Weather.objects.create(**validated_data)
