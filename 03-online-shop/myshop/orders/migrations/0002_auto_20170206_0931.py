# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='update',
            new_name='updated',
        ),
    ]
