from decimal import Decimal
from uuid import uuid4

import django_heroku
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Exists, OuterRef
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from moneyed import Money
from tinymce import models as tinymce_models
from Products.models import Units

from Products.querysets.product_queryset import ProductQuerySet


class Product(models.Model):
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    name = models.CharField(max_length=100, verbose_name="nombre")
    short_description = models.CharField(max_length=255, verbose_name="descripcion corta")
    description = tinymce_models.HTMLField(verbose_name="descripcion larga")
    price = MoneyField(max_digits=12, decimal_places=2, validators=[MinMoneyValidator(Decimal("0.01"))],
                       verbose_name="precio")
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)] )

    width = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    height = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    depth = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    constante = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    objects = ProductQuerySet.as_manager()

    def __str__(self):
        return self.name

    def cover_image(self):
        image = self.images.first()
        return image.url() if image else '/static/no_image.jpg'

    def price_with_discount(self):
        # da el precio con descuento en la moneda del producto
        return self.price * (100 - self.discount) / 100

    def sale_price(self):
        # da el precio con descuento en pesos argentinos

        if self.price.currency.code == 'ARS':
            return self.price_with_discount()

        # convertir dolares a pesos
        return Money(self.price_with_discount().amount * 150, "ARS")

    def shipping_price(self):
        # TODO: meter calculo de envio cuando se implemente
        return Money(self.width * self.depth * self.height * self.constante, "ARS")

    def variants_with_values(self):
        from Products.models import ProductVariantValue
        return self.variants.filter(Exists(ProductVariantValue.objects.filter(variant__id=OuterRef('pk'))))


class ProductVideo(models.Model):
    class Meta:
        verbose_name = "video del producto"
        verbose_name_plural = "videos del producto"

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="videos")
    externalUri = models.URLField(max_length=200, null=True, blank=True, verbose_name="Video externo")


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

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=path_and_rename, null=True, blank=True, verbose_name="Imagen")
    externalUri = models.URLField(max_length=200, null=True, blank=True, verbose_name="Imagen externa")

    def clean(self):
        if not self.image and not self.externalUri:
            raise ValidationError("Tiene que subir una imágen o ingresar una url")

    def url(self):
        return self.externalUri or self.image.url
