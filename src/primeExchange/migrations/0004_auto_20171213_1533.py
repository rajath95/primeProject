# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0003_commodities_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='specializatonMaster',
            fields=[
                ('recordID', models.AutoField(serialize=False, primary_key=True)),
                ('specializationID', models.IntegerField()),
                ('specializationName', models.CharField(max_length=100)),
                ('UpdatedOn', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 15, 33, 29, 940716), null=True),
        ),
        migrations.AddField(
            model_name='doctormaster',
            name='doctorContact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctormaster',
            name='doctorEmpID',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='servicecodemaster',
            name='BusinessUnitCategory',
            field=models.CharField(default=1, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicecodemaster',
            name='serviceCodeCategoryID',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
