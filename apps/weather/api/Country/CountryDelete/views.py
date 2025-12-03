from config.permissions import IsAdminUser
from rest_framework.generics import RetrieveDestroyAPIView
from .serializers import CountryDeleteAPISerializer
from apps.weather.models import Country


class CountryDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDeleteAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'
