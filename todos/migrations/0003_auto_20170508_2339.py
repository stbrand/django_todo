# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 21:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todoitem_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='value',
            new_name='title',
        ),
    ]
