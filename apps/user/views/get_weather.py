from rest_framework.views import APIView

from config.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from ..serializers.get_weather import GetWeatherSerializer


class GetWeatherAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        weather = request.user.get_weather

        if not weather:
            return Response(
                {"detail": "Ushbu manzil uchun ob-havo ma'lumoti mavjud emas!"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = GetWeatherSerializer(weather)

        return Response(serializer.data, status=status.HTTP_200_OK)
