from rest_framework.serializers import ModelSerializer
from .models import Inventory

class InventorySerializer (ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
