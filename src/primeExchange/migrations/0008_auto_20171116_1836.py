# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0007_auto_20171116_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 23, 933551)),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 933877, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 933602, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 933717, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 933520, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 23, 933578), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 936036, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 936370, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 936087, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 936215, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 935997, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 23, 936062), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 23, 934734)),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 935136, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 934786, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 934899, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 934704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 934761, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 931815, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 932185, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 931880, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 932025, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 23, 931782, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 23, 931841), null=True),
        ),
    ]
