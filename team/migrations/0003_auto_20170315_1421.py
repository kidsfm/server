# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20170315_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Member'),
        ),
    ]