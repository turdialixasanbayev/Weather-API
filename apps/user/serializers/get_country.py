from rest_framework import serializers


class GetCountrySerializer(serializers.Serializer):
    name = serializers.CharField()
