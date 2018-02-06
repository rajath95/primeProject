# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0003_auto_20180205_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(null=True, default=datetime.datetime(2018, 2, 4, 16, 40, 49, 915909)),
        ),
    ]
