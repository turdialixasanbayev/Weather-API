from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer

class LoginView(views.APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
