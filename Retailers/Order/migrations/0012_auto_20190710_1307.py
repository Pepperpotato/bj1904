# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-10 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0011_auto_20190710_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertwenty',
            name='ordertime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
