# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-06 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0016_auto_20190706_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='commoditycategoriestwo',
            name='is_show',
            field=models.IntegerField(default=0),
        ),
    ]
