# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='card_name',
            field=models.CharField(default=12, max_length=55),
            preserve_default=False,
        ),
    ]
