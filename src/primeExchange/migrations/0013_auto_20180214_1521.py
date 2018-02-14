# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0012_auto_20180214_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='clientID',
            field=models.CharField(default='gleneagles_lbn', max_length=30),
        ),
        migrations.AlterField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 13, 15, 21, 23, 542070), null=True),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 545602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='NextVisitDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 545957, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 545653, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='PaymentDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 545795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 545571, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='TimeOfBilling',
            field=models.TimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 15, 21, 23, 545626)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 543999, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='NextVisitDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 544455, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 544055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PaymentDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 544291, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 9, 51, 23, 543964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='TimeOfBilling',
            field=models.TimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 15, 21, 23, 544023)),
        ),
    ]
