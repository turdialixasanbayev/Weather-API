from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from ..serializers.get_country import GetCountrySerializer


class GetCountryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        country = request.user.get_country

        if not country:
            return Response(
                {"detail": "Foydalanuvchi mamlakati mavjud emas!"},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = {"name": country.name}

        serializer = GetCountrySerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
