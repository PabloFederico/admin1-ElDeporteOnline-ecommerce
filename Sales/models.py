from django.conf import settings
from django.db import models
from djmoney.models.fields import MoneyField

from Products.models import Product, ProductVariantValue


class Cart:
    """Stores products + quantity as a list of tuples (product_id, quantity)"""

    def __init__(self, request):
        self.request = request
        self.products = []
        self._products_cached = None
        self._load()

    def _save(self):
        self._products_cached = None
        self.request.session[settings.CART_SESSION_VARIABLE] = self.products

    def _load(self):
        self._products_cached = None
        self.products = self.request.session.get(settings.CART_SESSION_VARIABLE, [])

    def clear(self):
        self._products_cached = None
        self.request.session[settings.CART_SESSION_VARIABLE] = []

    def get_products(self):
        """
        Returns a list of the products in the cart, with the format:
            {"product": product_model, "quantity": number}
        """
        if self._products_cached:
            return self._products_cached

        data = []
        for product_data in self.products:
            product = Product.objects.filter(id=product_data[0]).first()
            if not product:
                continue
            quantity = product_data[1]
            data.append({
                "product": product,
                "subTotal": product.sale_price() * quantity,
                "quantity": quantity,
                "priceEnvio": product.shipping_price() * quantity,
                "variants": ProductVariantValue.objects.filter(id__in=product_data[2]),
            })

        self._products_cached = data
        return data

    def get_total(self):
        total = 0
        totalEnvio = 0
        for product_data in self.get_products():
            total = total + product_data["subTotal"]
            totalEnvio = totalEnvio + product_data["priceEnvio"]

        data = {
            "total": total,
            "totalEnvio": totalEnvio
        }
        return data

    def add_product(self, product, quantity, variants):
        variant_ids = self._map_variants(variants)
        for i, data in enumerate(self.products):
            if data[0] == product.id and data[2] == variant_ids:
                # product already in cart
                new_product_data = [product.id, quantity + data[1], variant_ids]
                self.products[i] = new_product_data
                self._save()
                return

        new_product_data = [product.id, quantity, variant_ids]
        self.products.append(new_product_data)
        self._save()

    def remove_product(self, product, variants):
        variant_ids = self._map_variants(variants)
        self.products = list(filter(lambda x: x[0] != product.id or x[2] != variant_ids, self.products))
        self._save()

    def count(self):
        return len(self.get_products())

    def _map_variants(self, variants):
        return list(sorted(map(lambda v: v.id, variants)))


class Sale(models.Model):
    """representa una compra"""

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    date = models.DateTimeField(auto_now_add=True, verbose_name="fecha")
    name = models.CharField(max_length=255, verbose_name="nombre del cliente")
    address = models.CharField(max_length=255, verbose_name="domicilio de entrega")
    shipping_price = MoneyField(max_digits=12, decimal_places=2, verbose_name="envio")

    def __str__(self):
        return self.date.__str__()

    def total(self):
        return sum([item.price for item in self.items.all()])


class Item(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="producto")
    quantity = models.PositiveIntegerField(verbose_name="cantidad")
    price = MoneyField(max_digits=12, decimal_places=2, verbose_name="precio pagado")
    product_name = models.CharField(max_length=255, verbose_name="nombre del producto")  # por si se elimina el producto

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"
