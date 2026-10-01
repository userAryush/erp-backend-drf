import django_filters
from django.db.models import F

from .models import Inventory

class InventoryFilter(django_filters.FilterSet):
    low_stock = django_filters.BooleanFilter(
        method='filter_low_stock',
    )
    
    class Meta:
        model = Inventory
        fields = ['product', 'warehouse']
        
    def filter_low_stock(self, queryset, name, value):
        if not value:
            return queryset
        
        return queryset.filter(quantity__lt= F("product__minimum_stock_level"))