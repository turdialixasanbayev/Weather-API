from config.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from .serializers import CountryListAPISerializer
from apps.weather.models import Country


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListAPISerializer
    # permission_classes = [IsAdminUser]
    # pagination_class = None
