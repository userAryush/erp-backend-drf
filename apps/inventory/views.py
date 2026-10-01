from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from Base.permissions import IsAdminOrInventoryManager

from .filters import InventoryFilter
from .models import Inventory
from .serializers import InventorySerializer


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.select_related(
        "product",
        "warehouse",
    )
    serializer_class = InventorySerializer
    permission_classes = [IsAdminOrInventoryManager]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = InventoryFilter

    search_fields = [
        "product__name",
        "product__sku",
        "product__barcode",
        "warehouse__name",
        "warehouse__code",
    ]

    ordering_fields = [
        "quantity",
        "created_at",
        "updated_at",
    ]

    ordering = ["product", "warehouse"]