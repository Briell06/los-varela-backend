from rest_framework import viewsets
from django.db.models import Q
from api.models import Category, Product
from api.serializer import CategorySerializer, ProductSerializer


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True).order_by("title")


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).order_by("-updated_at")
        search = self.request.query_params.get("query")
        if search is not None:
            queryset = queryset.filter(
                Q(is_active=True) & Q(title__icontains=search)
                | Q(category__title__icontains=search)
            ).order_by("-updated_at")
        return queryset
