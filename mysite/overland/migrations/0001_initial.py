# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=30)),
                ('last', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=4)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
            ],
        ),
    ]
