# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0006_auto_20171116_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 21, 189743)),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 190062, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 189791, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 189905, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 189715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historicalbillingdata',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 21, 189768), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 192157, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 192526, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 192208, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 192369, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 192129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nottobepredictedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 21, 192181), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 21, 190909)),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 191300, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 190960, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 191073, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 190882, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tobepredictedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 190936, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 188088, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 188430, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 188147, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 188267, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 16, 13, 6, 21, 188055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 11, 16, 18, 36, 21, 188113), null=True),
        ),
    ]
