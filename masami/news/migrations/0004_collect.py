# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180510_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('news_id', models.CharField(max_length=20)),
            ],
        ),
    ]
