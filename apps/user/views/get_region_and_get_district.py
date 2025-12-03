from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from ..serializers.get_region_and_get_district import (
    GetRegionSerializer,
    GetDistrictSerializer,
)


class GetDistrictAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.get_district:
            return Response(
                {"detail": "District mavjud emas!"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = GetDistrictSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetRegionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.get_region:
            return Response(
                {"detail": "Region mavjud emas!"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = GetRegionSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
