# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-05 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0010_auto_20190705_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='historicalprices',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='weightprice',
        ),
        migrations.AddField(
            model_name='commoditycategoriestwo',
            name='historicalprices',
            field=models.IntegerField(default=0),
        ),
    ]
