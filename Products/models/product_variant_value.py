from django.db import models

from Products.models import ProductVariant


class ProductVariantValue(models.Model):
    name = models.CharField(max_length=255)
    variant = models.ForeignKey(ProductVariant, related_name="values", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.variant} = {self.name}"
