# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_group',
            name='group',
        ),
        migrations.RemoveField(
            model_name='user_group',
            name='user',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='User_group',
        ),
    ]
