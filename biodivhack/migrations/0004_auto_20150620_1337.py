# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biodivhack', '0003_auto_20150620_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='statuschangeevent',
            name='status',
            field=models.CharField(default=b'Unreviewed', max_length=100),
        ),
        migrations.AlterField(
            model_name='statuschangeevent',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 20, 13, 37, 41, 512276)),
        ),
    ]
