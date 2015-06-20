# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biodivhack', '0002_paper_doi'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusChangeEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=1000)),
                ('date', models.DateField(default=datetime.datetime(2015, 6, 20, 13, 32, 24, 68416))),
            ],
        ),
        migrations.AlterField(
            model_name='paper',
            name='status',
            field=models.CharField(default=b'Unreviewed', max_length=100),
        ),
        migrations.AddField(
            model_name='statuschangeevent',
            name='paper',
            field=models.ForeignKey(to='biodivhack.Paper'),
        ),
    ]
