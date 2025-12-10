from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from config.permissions import IsAuthenticated
from .serializers import LogoutSerializer

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
