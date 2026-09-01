from django.db import models
from Base.models import BaseModel
# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=255, unique = True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Brand(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Product(BaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )
    
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="products"
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    barcode = models.CharField(max_length=100, unique=True, blank=True, null=True)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2)
    minimum_stock_level = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.category.name} -- {self.is_available and 'Available' or 'Not Available'}"

