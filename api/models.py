import uuid

from django.db import models
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category_images/")

    def __str__(self):
        return self.title

    def mostrar_imagen(self):
        return format_html(f"<img src='{self.image.url}' width='100' height='100' />")


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name="Nombre del producto")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    description = models.TextField(verbose_name="Descripción del producto")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    image = models.ImageField(
        upload_to="product_images/", verbose_name="Imagen del producto"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Categoría",
    )

    def __str__(self):
        return self.title

    def mostrar_imagen(self):
        return format_html(f"<img src='{self.image.url}' width='100' height='100' />")
