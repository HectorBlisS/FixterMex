# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160826_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='theater',
            field=models.ManyToManyField(related_name='movies', to='main.Theather'),
        ),
    ]
