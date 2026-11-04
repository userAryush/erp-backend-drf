
from django.contrib import admin

from .models import PurchaseOrder, PurchaseOrderItem


class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem
    extra = 0


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "supplier",
        "warehouse",
        "status",
        "created_at",
    )
    list_filter = (
        "status",
        "supplier",
        "warehouse",
        "created_at",
    )
    search_fields = (
        "supplier__company_name",
        "warehouse__name",
        "notes",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    inlines = [PurchaseOrderItemInline]


@admin.register(PurchaseOrderItem)
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "purchase_order",
        "product",
        "quantity",
        "unit_cost",
    )
    list_filter = (
        "product",
    )
    search_fields = (
        "product__name",
        "product__sku",
        "purchase_order__supplier__company_name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
