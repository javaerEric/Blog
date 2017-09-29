# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20170929_0404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='keywords',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
