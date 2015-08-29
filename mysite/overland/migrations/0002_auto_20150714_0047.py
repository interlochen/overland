# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('overland', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='first',
            new_name='names',
        ),
        migrations.RemoveField(
            model_name='application',
            name='last',
        ),
        migrations.AddField(
            model_name='application',
            name='useremail',
            field=models.EmailField(default=datetime.datetime(2015, 7, 14, 0, 47, 27, 661162, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
    ]
