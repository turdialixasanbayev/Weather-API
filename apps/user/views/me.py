from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from ..serializers.me import UserProfileSerializer


class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {"email": request.user.get_profile['email']}
        serializer = UserProfileSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
