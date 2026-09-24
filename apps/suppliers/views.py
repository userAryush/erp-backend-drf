from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import Supplier, SupplierProduct
from .serializers import SupplierSerializer, SupplierProductSerializer
from Base.permissions import IsAdminOrSupplierManager


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAdminOrSupplierManager]


class SupplierProductViewSet(ModelViewSet):
    queryset = SupplierProduct.objects.select_related(
        "supplier",
        "product",
    )
    serializer_class = SupplierProductSerializer
    permission_classes = [IsAdminOrSupplierManager]