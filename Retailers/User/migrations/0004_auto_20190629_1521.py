# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-29 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20190629_1519'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_collections',
            new_name='User_collection',
        ),
        migrations.AlterModelTable(
            name='user_collection',
            table='user_collection',
        ),
    ]
