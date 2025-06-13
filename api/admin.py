from django.contrib import admin

from api.models import Category, Product

admin.site.site_header = "Los Varela"
admin.site.site_title = "Los Varela"
admin.site.index_title = "Los Varela"


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "mostrar_imagen")
    search_fields = ("title",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "mostrar_imagen",
        "price",
        "category",
    )
    list_filter = ("category__title",)
    search_fields = ("title", "price", "category__title")
    prepopulated_fields = {"slug": ("title",)}
