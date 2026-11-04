
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from Base.permissions import IsAdminOrInventoryManager

from .filters import PurchaseOrderFilter, PurchaseOrderItemFilter
from .models import PurchaseOrder, PurchaseOrderItem
from .serializers import (
    PurchaseOrderSerializer,
    PurchaseOrderItemSerializer,
)


class PurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.select_related(
        "supplier",
        "warehouse",
    ).prefetch_related(
        "items__product",
    )
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAdminOrInventoryManager]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = PurchaseOrderFilter

    search_fields = [
        "supplier__company_name",
        "warehouse__name",
        "notes",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]


class PurchaseOrderItemViewSet(ModelViewSet):
    queryset = PurchaseOrderItem.objects.select_related(
        "purchase_order",
        "purchase_order__supplier",
        "product",
    )
    serializer_class = PurchaseOrderItemSerializer
    permission_classes = [IsAdminOrInventoryManager]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = PurchaseOrderItemFilter

    search_fields = [
        "product__name",
        "product__sku",
        "purchase_order__supplier__company_name",
    ]

    ordering_fields = [
        "quantity",
        "unit_cost",
        "created_at",
    ]
    ordering = ["purchase_order", "product"]
