from django_filters import FilterSet

from .models import Supplier, SupplierProduct

class SupplierFilter(FilterSet):
    class Meta:
        model = Supplier
        fields = []