# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-28 18:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0014_auto_20160827_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='figure',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='figure',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 8, 28, 18, 2, 29, 268970, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='simulation_input',
            unique_together=set([('simulation', 'field')]),
        ),
    ]