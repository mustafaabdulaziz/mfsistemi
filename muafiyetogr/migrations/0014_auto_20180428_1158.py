# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-28 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muafiyetogr', '0013_auto_20180428_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogrenci',
            name='ogr_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
