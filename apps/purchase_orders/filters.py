
import django_filters

from .models import PurchaseOrder, PurchaseOrderItem


class PurchaseOrderFilter(django_filters.FilterSet):
    created_after = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__gte",
    )
    created_before = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__lte",
    )

    class Meta:
        model = PurchaseOrder
        fields = [
            "supplier",
            "warehouse",
            "status",
        ]


class PurchaseOrderItemFilter(django_filters.FilterSet):
    class Meta:
        model = PurchaseOrderItem
        fields = [
            "purchase_order",
            "product",
        ]
