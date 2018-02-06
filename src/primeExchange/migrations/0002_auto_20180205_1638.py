# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalRevenue',
            fields=[
                ('recordID', models.AutoField(serialize=False, primary_key=True)),
                ('month', models.CharField(max_length=3, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default='1')),
                ('week', models.CharField(max_length=3, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1')),
                ('avg_pharma', models.IntegerField(null=True)),
                ('avg_lab', models.IntegerField(null=True)),
                ('avg_rad', models.IntegerField(null=True)),
                ('act_pharma', models.IntegerField(null=True)),
                ('act_lab', models.IntegerField(null=True)),
                ('act_rad', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specializatonMaster',
            fields=[
                ('recordID', models.AutoField(serialize=False, primary_key=True)),
                ('specializationID', models.IntegerField()),
                ('specializationName', models.CharField(max_length=100)),
                ('UpdatedOn', models.DateTimeField(null=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='commodities',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(null=True, default=datetime.datetime(2018, 2, 4, 16, 38, 50, 110313)),
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
            field=models.CharField(max_length=100, default=1, null=True),
        ),
        migrations.AddField(
            model_name='servicecodemaster',
            name='serviceCodeCategoryID',
            field=models.CharField(max_length=100, default=1),
        ),
    ]
