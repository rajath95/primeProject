# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0004_auto_20171025_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(default='Prime_Administrator', max_length=30, choices=[('Prime_admin', 'Prime_Administrator'), ('Hospital_management', 'Hospital_Management'), ('Hospital_admin', 'Hospital_Administrator')]),
        ),
    ]
