import os
from decimal import Decimal
from uuid import uuid4

import django_heroku
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from tinymce import models as tinymce_models

from Products.querysets.product_queryset import ProductQuerySet


class Product(models.Model):
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    name = models.CharField(max_length=255, verbose_name="nombre")
    short_description = models.CharField(max_length=255, verbose_name="descripcion corta")
    description = tinymce_models.HTMLField(verbose_name="descripcion larga")
    price = MoneyField(max_digits=12, decimal_places=2, validators=[MinMoneyValidator(Decimal("0.01"))],
                       verbose_name="precio")

    objects = ProductQuerySet.as_manager()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'images/products/'
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return django_heroku.os.path.join(upload_to, filename)

    class Meta:
        verbose_name = "imagen del producto"
        verbose_name_plural = "imagenes del producto"
    description = models.CharField(max_length=255, verbose_name="descripcion")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=path_and_rename,null=True, blank=True, verbose_name="Imagen")
    externalUri = models.URLField(max_length=200, null=True, blank=True, verbose_name="Imagen externa")
