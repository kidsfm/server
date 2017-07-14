# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('frequency', models.ManyToManyField(to='schedule.Day')),
                ('team', models.ManyToManyField(to='team.Member')),
            ],
        ),
    ]