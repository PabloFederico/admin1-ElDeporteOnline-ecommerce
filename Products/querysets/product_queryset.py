from django.db import models
from django.db.models import F, Q, ExpressionWrapper, DecimalField

class ProductQuerySet(models.QuerySet):

    def for_catalog(self):
        return self.all().annotate(price_sale = ExpressionWrapper(F('price')*(100 - F('discount'))/100, output_field=DecimalField(decimal_places=2)))

    def order_by_price(self, order):
        if not order:
            return self

        sign = "" if order == "asc" else "-"
        return self.order_by(sign + 'price_currency', sign + 'price_sale')

    def filter_by_text(self, filtro):
        if not filtro:
            return self
        return self.filter(Q(name__icontains=filtro) | Q(description__icontains=filtro) | Q(short_description__icontains=filtro))