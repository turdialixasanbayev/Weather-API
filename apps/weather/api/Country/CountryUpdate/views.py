from config.permissions import IsAdminUser
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import CountryUpdateAPISerializer
from apps.weather.models import Country


class CountryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryUpdateAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'
