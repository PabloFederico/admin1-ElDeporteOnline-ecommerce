from decimal import Decimal

from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator

from Products.querysets.product_queryset import ProductQuerySet


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    price = MoneyField(max_digits=12, decimal_places=2, validators=[MinMoneyValidator(Decimal("0.01"))])
    hide_from_catalog = models.BooleanField(default=False)

    objects = ProductQuerySet.as_manager()

    def __str__(self):
        return self.name
