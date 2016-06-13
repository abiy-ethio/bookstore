# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20160408_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publiched_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 9, 6, 4, 6, 975000, tzinfo=utc)),
        ),
    ]
