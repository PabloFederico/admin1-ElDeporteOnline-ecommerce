# Generated by Django 3.1.2 on 2020-12-08 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0018_auto_20201205_1855'),
        ('Sales', '0002_auto_20201207_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='product_name',
            field=models.CharField(default='producto', max_length=255, verbose_name='nombre del producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.product', verbose_name='producto'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='cantidad'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha'),
        ),
    ]
