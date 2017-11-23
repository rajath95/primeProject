# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0010_doctormaster_servicecodemaster_smslookup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smslookup',
            name='doctorID',
            field=models.ForeignKey(to='primeExchange.doctorMaster'),
        ),
    ]
