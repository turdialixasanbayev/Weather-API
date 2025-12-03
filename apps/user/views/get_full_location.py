from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status


class UserLocationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        location = request.user.get_full_location

        if not location:
            return Response(
                {"detail": "Foydalanuvchi manzili belgilanmagan!"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(location, status=status.HTTP_200_OK)
