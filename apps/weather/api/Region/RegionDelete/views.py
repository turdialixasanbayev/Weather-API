from rest_framework.generics import RetrieveDestroyAPIView

from .serializers import RegionDeleteAPISerializer

from apps.weather.models import Region
from config.permissions import IsAdminUser


class RegionDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDeleteAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        return Region.objects.all().select_related('country')


as_view = RegionDestroyAPIView.as_view()
