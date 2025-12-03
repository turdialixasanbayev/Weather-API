from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from config.permissions import IsAuthenticated

from apps.weather.models import Village
from ..serializers.search_village import VillageSearchSerializer


class SearchVillageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.GET.get("query")

        if not query:
            return Response(
                {"detail": "Village nomini 'query' orqali yuboring!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            village = Village.objects.get(name__iexact=query)
        except Village.DoesNotExist:
            return Response(
                {"detail": "Bunday nomdagi village topilmadi!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        data = {
            "name": village.name,
            "district": village.district.name,
        }

        serializer = VillageSearchSerializer(data)

        return Response(
            {
                "success": True,
                "message": "Village topildi!",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
