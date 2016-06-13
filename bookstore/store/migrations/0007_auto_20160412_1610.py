# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0006_auto_20160409_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publshed_date', models.DateField(default=datetime.datetime(2016, 4, 12, 13, 10, 17, 237000, tzinfo=utc))),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='publiched_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 12, 13, 10, 17, 235000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(to='store.Book'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
