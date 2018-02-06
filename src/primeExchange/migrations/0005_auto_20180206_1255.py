# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0004_auto_20180205_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(null=True, default=datetime.datetime(2018, 2, 5, 12, 55, 25, 626005)),
        ),
    ]
