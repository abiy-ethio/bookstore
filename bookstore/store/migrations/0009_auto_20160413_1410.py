# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20160412_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default=b'books/slider3', upload_to=b'books/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publiched_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 13, 11, 10, 29, 621000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='publshed_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 13, 11, 10, 29, 622000, tzinfo=utc)),
        ),
    ]
