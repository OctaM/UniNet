# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default='Stire despre Ana', max_length=100),
            preserve_default=False,
        ),
    ]