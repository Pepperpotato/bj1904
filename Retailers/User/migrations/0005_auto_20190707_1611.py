# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-07 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20190707_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='certificate_down',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='certificate_top',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
