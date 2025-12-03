from rest_framework.views import APIView

from config.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status


class GetDistrictAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        district = request.user.get_district

        if not district:
            return Response(
                {"detail": "Foydalanuvchi tumani mavjud emas!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(district, status=status.HTTP_200_OK)


class GetRegionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        region = request.user.get_region

        if not region:
            return Response(
                {"detail": "Foydalanuvchi viloyati mavjud emas!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(region, status=status.HTTP_200_OK)
