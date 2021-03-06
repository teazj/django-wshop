# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-22 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20170720_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='cost_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='成本价'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='market_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='市场价'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='sales_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='售出数量'),
        ),
    ]
