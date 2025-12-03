from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from config.permissions import IsAuthenticated


class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(request.user.get_profile, status=status.HTTP_200_OK)
