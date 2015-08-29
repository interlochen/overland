# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overland', '0002_auto_20150714_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='year',
            field=models.IntegerField(default=2015),
        ),
    ]
