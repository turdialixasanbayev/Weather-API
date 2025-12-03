from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response


class GetVillageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        village = request.user.get_village

        if not village:
            return Response(
                {"detail": "Ushbu foydalanuvchida village mavjud emas!"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response({"village": village.name}, status=status.HTTP_200_OK)
