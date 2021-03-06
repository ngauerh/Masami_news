# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nid', models.IntegerField()),
                ('author', models.CharField(max_length=25)),
                ('comments', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='News1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=125)),
                ('url', models.TextField()),
                ('summary', models.TextField()),
                ('details', models.TextField()),
                ('source', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('news_time', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'n_news',
            },
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Niu',
        ),
    ]
