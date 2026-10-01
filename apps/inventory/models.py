from django.core.validators import MinValueValidator
from django.db import models

from Base.models import BaseModel
from apps.products.models import Product
from apps.warehouse.models import Warehouse


class Inventory(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="inventory_records",
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="inventory_records",
    )
    quantity = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "warehouse"],
                name="unique_product_warehouse_inventory",
            )
        ]
        ordering = ["product", "warehouse"]

    def __str__(self):
        return f"{self.product.name} - {self.warehouse.name}"