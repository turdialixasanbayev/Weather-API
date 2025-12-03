from rest_framework import serializers


class GetRegionSerializer(serializers.Serializer):
    name = serializers.CharField(source="get_region.name")


class GetDistrictSerializer(serializers.Serializer):
    name = serializers.CharField(source="get_district.name")
