# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-05 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0012_auto_20190705_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='attributeid',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='unit',
        ),
        migrations.AddField(
            model_name='commoditycategoriestwo',
            name='gid',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='commoditycategoriestwo',
            name='unit',
            field=models.CharField(default='件', max_length=20),
        ),
    ]
