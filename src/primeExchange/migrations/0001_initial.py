# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodities',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('commodity', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='doctorMaster',
            fields=[
                ('doctorID', models.AutoField(primary_key=True, serialize=False)),
                ('doctorName', models.CharField(max_length=100)),
                ('doctorDesignation', models.CharField(max_length=100, null=True)),
                ('doctorSpecialization', models.CharField(max_length=100, null=True)),
                ('UpdatedOn', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('role', models.CharField(default='Prime_Administrator', max_length=30, choices=[('Prime_admin', 'Prime_Administrator'), ('Hospital_management', 'Hospital_Management'), ('Hospital_admin', 'Hospital_Administrator')])),
                ('mobile', models.CharField(max_length=10)),
                ('office_contact', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='serviceCodeMaster',
            fields=[
                ('recordID', models.AutoField(primary_key=True, serialize=False)),
                ('serviceCode', models.CharField(max_length=100)),
                ('serviceName', models.CharField(max_length=500, null=True)),
                ('serviceCodeCategory', models.CharField(max_length=100, null=True)),
                ('UpdatedOn', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SMSlookup',
            fields=[
                ('recordID', models.AutoField(primary_key=True, serialize=False)),
                ('doctorName', models.CharField(max_length=100)),
                ('SMSContact', models.IntegerField()),
                ('UpdatedOn', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('doctor', models.ForeignKey(to='primeExchange.doctorMaster')),
            ],
        ),
    ]
