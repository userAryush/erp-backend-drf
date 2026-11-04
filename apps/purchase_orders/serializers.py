
from rest_framework import serializers

from .models import PurchaseOrder, PurchaseOrderItem


class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(many=True, read_only=True)

    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        read_only_fields = [
            "id",
            "status",
            "created_at",
            "updated_at",
        ]

    def get_total_amount(self, obj):
        total = sum(
            item.quantity * item.unit_cost
            for item in obj.items.all()
        )
        return total
