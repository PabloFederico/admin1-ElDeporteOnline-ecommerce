from django.db import models


class ProductQuerySet(models.QuerySet):

    def for_catalog(self):
        return self.all()

    def order_by_price(self, order):
        if not order:
            return self

        sign = "" if order == "asc" else "-"
        return self.order_by(sign + 'price_currency', sign + 'price')
