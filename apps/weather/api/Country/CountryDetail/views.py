from config.permissions import IsAdminUser
from rest_framework.generics import RetrieveAPIView
from .serializers import CountryRetrieveAPISerializer
from apps.weather.models import Country


class CountryRetrieveAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryRetrieveAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'
