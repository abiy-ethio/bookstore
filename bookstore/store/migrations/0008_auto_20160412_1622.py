# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20160412_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(to='store.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publiched_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 12, 13, 22, 46, 572000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='publshed_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 12, 13, 22, 46, 573000, tzinfo=utc)),
        ),
    ]
