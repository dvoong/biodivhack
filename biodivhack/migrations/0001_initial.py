# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeywordAnalysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('abstract', models.CharField(max_length=10000)),
                ('url', models.URLField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reviewer', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('paper', models.ForeignKey(to='biodivhack.Paper')),
            ],
        ),
        migrations.AddField(
            model_name='keywordanalysis',
            name='paper',
            field=models.ForeignKey(to='biodivhack.Paper'),
        ),
    ]
