# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-08 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0017_commoditycategoriestwo_is_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='commoditycategoriestwo',
            name='stockprice',
            field=models.IntegerField(default=10),
        ),
    ]
