# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-05 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20160628_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=b''),
        ),
    ]
