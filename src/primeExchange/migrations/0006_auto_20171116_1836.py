# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0005_badbillingrecord_historicalbillingdata_nottobepredictedbillingrecord_rawbillingrecord_rawerrorrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 9, 568259)),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 568577, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 568311, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 568423, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 568232, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 9, 568285), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 570638, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 570955, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 570687, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 570800, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 570609, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 9, 570662), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 9, 569418)),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 569804, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 569469, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 569582, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 569390, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 569445, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 566585, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 566940, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 566655, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 566780, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 9, 566543, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 9, 566619), null=True),
        ),
    ]
