# Generated by Django 3.1.2 on 2020-12-01 00:07

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0014_auto_20201129_1935'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='productimage',
            managers=[
                ('objectsProductsImages', django.db.models.manager.Manager()),
            ],
        ),
    ]
