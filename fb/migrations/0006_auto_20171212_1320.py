# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-12 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0005_contactbook2_contacturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacturl',
            name='url',
            field=models.CharField(blank=True, max_length=255, verbose_name='傳送url'),
        ),
    ]
