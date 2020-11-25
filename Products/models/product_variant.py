from django.db import models

from Products.models import Product


class ProductVariant(models.Model):
    class Meta:
        verbose_name = "variante de producto"
        verbose_name_plural = "variantes de producto"

    name = models.CharField(max_length=255, verbose_name="nombre")
    product = models.ForeignKey(Product, related_name="variants", on_delete=models.CASCADE, verbose_name="producto")

    def __str__(self):
        return f"{self.product}: {self.name}"
