# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=8, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='publiched_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 7, 14, 46, 47, 886000, tzinfo=utc)),
        ),
    ]
