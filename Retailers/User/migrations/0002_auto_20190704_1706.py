# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-04 17:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reg_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='safety_grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[(1, '男'), (2, '女'), (0, '保密')], default=1, max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.CharField(default='/admin/upload/avatar_blank.gif', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='vip_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_account',
            name='bankcard_id',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='user_account',
            name='integral_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='location',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='user_collection',
            name='collection_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user_grade',
            name='change_source',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_grade',
            name='changed_grade',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user_grade',
            name='growth_value',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user_notice',
            name='sendtime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user_offer',
            name='offer_content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_offer',
            name='offer_door',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_offer',
            name='offer_money',
            field=models.IntegerField(null=True),
        ),
    ]
