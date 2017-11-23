# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0008_auto_20171116_1836'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BadBillingRecord',
        ),
        migrations.DeleteModel(
            name='HistoricalBillingData',
        ),
        migrations.DeleteModel(
            name='NotTobePredictedBillingRecord',
        ),
        migrations.DeleteModel(
            name='RawBillingRecord',
        ),
        migrations.DeleteModel(
            name='rawErrorRecord',
        ),
        migrations.DeleteModel(
            name='TobePredictedBillingRecord',
        ),
        migrations.DeleteModel(
            name='ValidatedBillingRecord',
        ),
    ]
