from django.db import models


class ProductQuerySet(models.QuerySet):

    def for_catalog(self):
        return self.all()
