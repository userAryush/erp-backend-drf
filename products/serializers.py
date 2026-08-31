from .models import Category, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()  
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
        