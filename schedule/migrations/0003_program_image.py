# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20170308_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='image',
            field=models.ImageField(default='img/schedule/program', upload_to='img/schedule/program'),
            preserve_default=False,
        ),
    ]