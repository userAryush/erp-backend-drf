from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer
from Base.permissions import  IsAdminOrInventoryManager
from .filters import ProductFilter


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrInventoryManager]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrInventoryManager]    
    
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = ProductFilter

    search_fields = [
        "name",
        "barcode",
        "category__name",
        "brand__name",
    ]

    ordering_fields = [
        "name",
        "created_at",
        "selling_price",
    ]

    ordering = ["name"]
    
    
    
class BrandView(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminOrInventoryManager()]
        return [AllowAny()]
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            brand = serializer.save()
            return Response(
                BrandSerializer(brand).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)