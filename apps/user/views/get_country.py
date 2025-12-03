from rest_framework.views import APIView

from config.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status


class GetCountryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        country = request.user.get_country

        if not country:
            return Response(
                {"detail": "Foydalanuvchi mamlakati mavjud emas!"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(country, status=status.HTTP_200_OK)
