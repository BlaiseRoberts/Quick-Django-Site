# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artist_name',
            new_name='artist_text',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='song_title',
            new_name='song_text',
        ),
    ]
