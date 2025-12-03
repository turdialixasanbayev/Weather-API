from rest_framework import serializers


class VillageSearchSerializer(serializers.Serializer):
    name = serializers.CharField()
    district = serializers.CharField()
