# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
