# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-05 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0005_auto_20190704_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='commoditycategoriestwo',
            name='sort',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
