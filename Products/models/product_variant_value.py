from django.db import models

from Products.models import ProductVariant


class ProductVariantValue(models.Model):
    class Meta:
        verbose_name = "valor de variante de producto"
        verbose_name_plural = "valores de variantes de producto"

    name = models.CharField(max_length=255, verbose_name="nombre")
    variant = models.ForeignKey(ProductVariant, related_name="values", on_delete=models.CASCADE,
                                verbose_name="variante de producto")

    def __str__(self):
        return f"{self.variant.name}: {self.name}"
