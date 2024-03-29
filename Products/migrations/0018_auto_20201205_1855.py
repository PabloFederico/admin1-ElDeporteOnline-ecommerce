# Generated by Django 3.1.2 on 2020-12-05 21:55

from django.db import migrations
from django.db.models import Q


def delete_invalid_images(apps, schema_editor):
    ProductImage = apps.get_model("Products", "ProductImage")
    ProductImage.objects.filter(Q(image__isnull=True) | Q(image=""), externalUri__isnull=True).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('Products', '0017_remove_productimage_description'),
    ]

    operations = [
        migrations.RunPython(delete_invalid_images, migrations.RunPython.noop)
    ]
