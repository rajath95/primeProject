# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0004_auto_20171213_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(null=True, default=datetime.datetime(2017, 12, 12, 15, 52, 23, 764)),
        ),
    ]
