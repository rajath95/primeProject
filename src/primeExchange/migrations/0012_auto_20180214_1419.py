# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0011_auto_20180214_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 13, 14, 19, 24, 514604), null=True),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 518143, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='NextVisitDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 518499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 518199, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='PaymentDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 518342, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 518113, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='TimeOfBilling',
            field=models.TimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 14, 19, 24, 518168)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 516529, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='NextVisitDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 517015, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 516589, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PaymentDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 516847, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 49, 24, 516497, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='TimeOfBilling',
            field=models.TimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 14, 19, 24, 516555)),
        ),
    ]
