# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0009_auto_20171123_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorMaster',
            fields=[
                ('doctorID', models.AutoField(serialize=False, primary_key=True)),
                ('doctorName', models.CharField(max_length=100)),
                ('doctorDesignation', models.CharField(max_length=100, null=True)),
                ('doctorSpecialization', models.CharField(max_length=100, null=True)),
                ('UpdatedOn', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='serviceCodeMaster',
            fields=[
                ('recordID', models.AutoField(serialize=False, primary_key=True)),
                ('serviceCode', models.CharField(max_length=100)),
                ('serviceName', models.CharField(max_length=500, null=True)),
                ('serviceCodeCategory', models.CharField(max_length=100, null=True)),
                ('UpdatedOn', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SMSlookup',
            fields=[
                ('recordID', models.AutoField(serialize=False, primary_key=True)),
                ('doctorID', models.IntegerField()),
                ('doctorName', models.CharField(max_length=100)),
                ('SMSContact', models.IntegerField()),
                ('UpdatedOn', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
