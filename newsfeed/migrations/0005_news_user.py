# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0004_auto_20161213_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.User'),
            preserve_default=False,
        ),
    ]
