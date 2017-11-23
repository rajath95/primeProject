# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0011_auto_20171123_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smslookup',
            old_name='doctorID',
            new_name='doctor',
        ),
    ]
