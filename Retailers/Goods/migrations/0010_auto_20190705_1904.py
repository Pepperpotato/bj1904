# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-05 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0009_auto_20190705_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commoditycategoriestwo',
            name='brandid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='commoditycategoriestwo',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commoditycategoriestwo',
            name='specification_id',
            field=models.IntegerField(),
        ),
    ]