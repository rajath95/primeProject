# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0009_auto_20180209_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='rawErrorRecord',
            fields=[
                ('ErrorRecordID', models.AutoField(serialize=False, primary_key=True)),
                ('ClientID', models.CharField(max_length=30, default='gleneagles_lbn')),
                ('JSONString', models.CharField(max_length=2000)),
                ('ErrorMessage', models.CharField(max_length=2000)),
                ('UpdatedOn', models.DateTimeField(null=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(null=True, default=datetime.datetime(2018, 2, 13, 14, 6, 11, 35372)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 38947, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='NextVisitDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 39301, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 39001, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='PaymentDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 39143, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 38915, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predictedcommunicateddata',
            name='TimeOfBilling',
            field=models.TimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 14, 6, 11, 38973)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 37348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='NextVisitDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 37797, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 37408, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PaymentDate',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 37635, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 14, 8, 36, 11, 37314, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='TimeOfBilling',
            field=models.TimeField(null=True, verbose_name=datetime.datetime(2018, 2, 14, 14, 6, 11, 37374)),
        ),
    ]
