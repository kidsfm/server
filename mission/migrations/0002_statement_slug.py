# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 17:03
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
    ]
