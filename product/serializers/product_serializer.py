from rest_framework import serializers
from product.models import Product, Category
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'active', 'category', 'categories_id']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories_id', [])
        product = Product.objects.create(**validated_data)
        for category in categories_data:
            product.category.add(category)
        return product
