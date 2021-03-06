# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-09 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=125)),
                ('ip', models.GenericIPAddressField()),
                ('avatar', models.CharField(max_length=125)),
                ('is_activity', models.IntegerField()),
                ('power', models.CharField(max_length=125)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('login_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
