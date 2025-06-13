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
            "price",
            "category",
            "image",
            "slug",
            "description",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
        )
