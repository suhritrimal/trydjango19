# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 16:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 1, 10, 16, 57, 36, 303781, tzinfo=utc)),
            preserve_default=False,
        ),
    ]