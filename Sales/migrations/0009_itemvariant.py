# Generated by Django 3.1.2 on 2020-12-09 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0018_auto_20201205_1855'),
        ('Sales', '0008_auto_20201208_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_name', models.CharField(max_length=255, verbose_name='nombre de la variante')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='Sales.item')),
                ('variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.productvariantvalue', verbose_name='variante')),
            ],
        ),
    ]
