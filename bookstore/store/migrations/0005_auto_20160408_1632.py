# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20160408_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publiched_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 8, 13, 32, 19, 750000, tzinfo=utc)),
        ),
    ]
