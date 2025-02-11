# Generated by Django 5.1.5 on 2025-02-03 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_cartproducts_product_alter_cartproducts_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproducts',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.productprice'),
        ),
        migrations.AddField(
            model_name='commune',
            name='inpc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='commune',
            name='polygon',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moughataa',
            name='inpc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='moughataa',
            name='polygon',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wilaya',
            name='inpc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='wilaya',
            name='polygon',
            field=models.TextField(blank=True, null=True),
        ),
    ]
