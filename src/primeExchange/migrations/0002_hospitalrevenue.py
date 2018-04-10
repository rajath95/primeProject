# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalRevenue',
            fields=[
                ('recordID', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=3, default='1')),
                ('week', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=3, default='1')),
                ('avg_pharma', models.IntegerField(null=True)),
                ('avg_lab', models.IntegerField(null=True)),
                ('avg_rad', models.IntegerField(null=True)),
                ('act_pharma', models.IntegerField(null=True)),
                ('act_lab', models.IntegerField(null=True)),
                ('act_rad', models.IntegerField(null=True)),
            ],
        ),
    ]