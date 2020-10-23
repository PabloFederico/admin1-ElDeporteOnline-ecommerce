from django.db import models


class ProductQuerySet(models.QuerySet):
    def for_catalog(self):
        return self.filter(hide_from_catalog=False)