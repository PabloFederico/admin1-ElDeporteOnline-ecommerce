from django.conf import settings

from Products.models import Product
from django.db import models


class Cart:
    """Stores products + quantity as a list of tuples (product_id, quantity)"""

    def __init__(self, request):
        self.request = request
        self.products = []
        self._load()

    def _save(self):
        self.request.session[settings.CART_SESSION_VARIABLE] = self.products

    def _load(self):
        self.products = self.request.session.get(settings.CART_SESSION_VARIABLE, [])

    def clear(self):
        self.request.session[settings.CART_SESSION_VARIABLE] = []

    def get_products(self):
        """
        Returns a list of the products in the cart, with the format:
            {"product": product_model, "quantity": number}
        """
        data = []
        for product_data in self.products:
            product = Product.objects.filter(id=product_data[0]).first()
            if not product:
                continue
            data.append({
                "product": product,
                "quantity": product_data[1]
            })
        return data

    def get_total(self):
        """
        Returns a list of the products in the cart, with the format:
            {"product": product_model, "quantity": number}
        """
        total = 0
        totalEnvio = 0
        for product_data in self.products:
            product = Product.objects.filter(id=product_data[0]).first()
            if not product:
                continue
            total = total + product.price * product_data[1]

        data = {
            "total": total,
            "totalEnvio": totalEnvio
        }
        return data

    def add_product(self, product, quantity):
        for i, data in enumerate(self.products):
            if data[0] == product.id:
                # product already in cart
                new_product_data = (product.id, quantity + data[1])
                self.products[i] = new_product_data
                self._save()
                return

        new_product_data = (product.id, quantity)
        self.products.append(new_product_data)
        self._save()

    def remove_product(self, product):
        self.products = list(filter(lambda x: x[0] != product.id, self.products))
        self._save()

    def count(self):
        return len(self.products)


class Sale(models.Model):
    """representa una compra"""
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date.__str__()


class Item(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

