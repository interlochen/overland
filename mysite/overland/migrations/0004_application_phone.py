# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('overland', '0003_auto_20150714_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='phone',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999")]),
        ),
    ]
