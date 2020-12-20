from django.db import models

from django.core.validators import MinValueValidator


class Units(models.Model):
    class Meta:
        verbose_name = "unidad de medida"
        verbose_name_plural = "unidaded de medida"

    name = models.CharField(max_length=255, verbose_name="nombre")
    constante = models.IntegerField(default=0, validators=[MinValueValidator(0)])