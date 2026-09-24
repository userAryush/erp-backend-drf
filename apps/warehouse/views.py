from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from Base.permissions import IsAdminOrInventoryManager

from .models import Warehouse
from .serializers import WarehouseSerializer


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAdminOrInventoryManager]

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ["name", "code", "address"]
    ordering_fields = ["name", "code", "created_at"]

    ordering = ["name"]