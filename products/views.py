from rest_framework.viewsets import ModelViewSet

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from Base.permissions import  IsAdminOrInventoryManager

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrInventoryManager]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrInventoryManager]    