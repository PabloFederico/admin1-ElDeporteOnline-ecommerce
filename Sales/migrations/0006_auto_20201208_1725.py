# Generated by Django 3.1.2 on 2020-12-08 20:25

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0005_auto_20201208_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='shipping_price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='ARS', max_digits=12, verbose_name='envio'),
        ),
        migrations.AddField(
            model_name='sale',
            name='shipping_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('ARS', 'Peso Argentino'), ('USD', 'US Dollar')], default='ARS', editable=False, max_length=3),
        ),
    ]
