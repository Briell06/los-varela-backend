from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from api.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    category = StringRelatedField()

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "fake_price",
            "price",
            "category",
            "image",
            "is_active",
            "slug",
            "description",
            "created_at",
            "updated_at",
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
            "is_active",
            "products",
            "created_at",
            "updated_at",
        )
