from django.db import models

from Products.models import Product


class ProductVariant(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, related_name="variants", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}: {self.name}"
