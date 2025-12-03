from rest_framework import serializers

from apps.weather.models import Weather


class GetWeatherSerializer(serializers.ModelSerializer):
    village = serializers.CharField(source="village.name")

    class Meta:
        model = Weather
        fields = [
            "village",
            "temperature",
            "feels_like",
            "humidity",
            "pressure",
            "wind_speed",
            "wind_deg",
            "visibility",
            "condition",
            "description",
            "sunrise",
            "sunset",
            "updated_at",
        ]
