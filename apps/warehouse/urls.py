from rest_framework.routers import DefaultRouter

from .views import WarehouseViewSet


router = DefaultRouter()
router.register("warehouses", WarehouseViewSet)

urlpatterns = router.urls