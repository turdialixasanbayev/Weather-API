from rest_framework_simplejwt.views import TokenVerifyView
from .serializers import CustomTokenVerifySerializer

class CustomTokenVerifyView(TokenVerifyView):
    serializer_class = CustomTokenVerifySerializer
