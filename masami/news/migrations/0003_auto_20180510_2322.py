# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180510_2320'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News1',
            new_name='News',
        ),
    ]
