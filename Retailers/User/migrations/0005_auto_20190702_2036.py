# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-02 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_user_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_account',
            name='uid',
        ),
        migrations.AddField(
            model_name='user_account',
            name='user',
            field=models.OneToOneField(db_column='uid', default=1, on_delete=django.db.models.deletion.CASCADE, to='User.User'),
        ),
        migrations.AlterField(
            model_name='user_account',
            name='bankcard_id',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_account',
            name='integral_id',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user_account',
            name='money',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user_account',
            name='pay_password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]