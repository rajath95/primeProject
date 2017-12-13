# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0002_hospitalrevenue'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodities',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]