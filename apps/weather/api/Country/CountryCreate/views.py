from config.permissions import IsAdminUser
from rest_framework.generics import CreateAPIView
from .serializers import CountryCreateAPISerializer
from apps.weather.models import Country


class CountryCreateAPIView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryCreateAPISerializer
    permission_classes = [IsAdminUser]
