# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0003_commodities'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodities',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
