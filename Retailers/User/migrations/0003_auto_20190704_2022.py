# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-04 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20190704_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_account',
            name='bankcard_id',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
    ]
