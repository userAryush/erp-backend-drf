from django.db import models

from Base.models import BaseModel
from accounts.models import User
from products.models import Product


class Supplier(BaseModel):
    """
    Represents a company that supplies products to our business.

    Supplier information is kept separate from the User model because
    multiple users could eventually belong to the same supplier company.
    Currently, we associate one supplier account with one supplier company.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="supplier_profile"
    )

    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["company_name"]

    def __str__(self):
        return self.company_name


class SupplierProduct(BaseModel):
    """
    Associates a supplier with the products they supply.

    A product may have multiple suppliers, each offering a different
    purchase cost and lead time.
    """

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="supplied_products"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="suppliers"
    )

    supplier_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    delivery_time_days = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("supplier", "product")
        ordering = ["supplier", "product"]

    def __str__(self):
        return f"{self.supplier.company_name} - {self.product.name}"