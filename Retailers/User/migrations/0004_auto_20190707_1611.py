# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-07 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20190704_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='certificate_down',
            field=models.CharField(default='2', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='certificate_top',
            field=models.CharField(default='1', max_length=200, null=True),
        ),
    ]
