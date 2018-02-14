# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0010_auto_20180214_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 13, 14, 19, 16, 909357), null=True),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 912930, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='NextVisitDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 913296, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 912983, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='PaymentDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 913132, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 912900, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='TimeOfBilling',
            field=models.TimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 14, 19, 16, 912954)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 911323, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='NextVisitDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 911788, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 911382, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PaymentDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 911616, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 16, 911289, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='TimeOfBilling',
            field=models.TimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 14, 19, 16, 911348)),
        ),
    ]
