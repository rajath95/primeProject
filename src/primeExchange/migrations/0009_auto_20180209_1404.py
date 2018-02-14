# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0008_auto_20180208_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictedCommunicatedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecordID', models.IntegerField()),
                ('ClientID', models.CharField(default='gleneagles_lbn', max_length=30)),
                ('UHID', models.IntegerField()),
                ('AdmissionNumber', models.BigIntegerField(default=999, null=True)),
                ('RegistrationDate', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 869878, tzinfo=utc))),
                ('RegistrationNumber', models.BigIntegerField()),
                ('BillingDate', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 869911, tzinfo=utc))),
                ('BillingNumber', models.BigIntegerField()),
                ('TimeOfBilling', models.TimeField(verbose_name=datetime.datetime(2018, 2, 9, 14, 4, 35, 869935), null=True)),
                ('PatientZIP', models.IntegerField(null=True)),
                ('PatientDateOfBirth', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 869961, tzinfo=utc), null=True)),
                ('PatientGender', models.CharField(max_length=30, null=True)),
                ('PatientName', models.CharField(default='NA', max_length=100)),
                ('PatientContact', models.CharField(default='9999999999', max_length=30)),
                ('ServiceCode', models.CharField(max_length=30)),
                ('ServiceName', models.CharField(max_length=100)),
                ('NumberOfUnitsOfService', models.IntegerField()),
                ('ServiceAmount', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('DoctorName', models.CharField(max_length=100)),
                ('FinalBillAmount', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('FinalDiscountAmount', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('PaymentMode', models.CharField(max_length=30, null=True)),
                ('PaymentAmount', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('PaymentDate', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 870106, tzinfo=utc), null=True)),
                ('FinalBillingID', models.BigIntegerField(null=True)),
                ('FinalEncounterID', models.BigIntegerField(null=True)),
                ('InsuranceCoverage', models.CharField(max_length=30, null=True)),
                ('EmployerBasedInsurance', models.CharField(max_length=30, null=True)),
                ('InsuranceCompanyName', models.CharField(max_length=100, null=True)),
                ('PatientEducation', models.CharField(max_length=30, null=True)),
                ('EmploymentType', models.CharField(max_length=30, null=True)),
                ('PatientEmployer', models.CharField(max_length=30, null=True)),
                ('PatientAnnualIncomeRange', models.IntegerField(null=True)),
                ('FrequencyOfGleneaglesVisit', models.CharField(max_length=30, null=True)),
                ('LifestylePattern', models.CharField(max_length=30, null=True)),
                ('TreatmentPlan', models.CharField(max_length=30, null=True)),
                ('Rx', models.CharField(max_length=30, null=True)),
                ('TestsPrescribed', models.CharField(max_length=30, null=True)),
                ('NextVisitDate', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 870268, tzinfo=utc), null=True)),
                ('Referrals', models.CharField(max_length=30, null=True)),
                ('JSONString', models.CharField(max_length=2000)),
                ('DataExchangeStatus', models.CharField(max_length=1000, null=True)),
                ('pd_CCHolderID', models.SmallIntegerField()),
                ('pd_patientAge', models.SmallIntegerField()),
                ('pd_doctorID', models.SmallIntegerField()),
                ('pd_specializationID', models.SmallIntegerField()),
                ('pd_weekDayID', models.SmallIntegerField()),
                ('pd_weatherTempID', models.SmallIntegerField()),
                ('pd_weatherDescID', models.SmallIntegerField()),
                ('pd_hospitalLoadID', models.SmallIntegerField()),
                ('pd_patientGenderID', models.SmallIntegerField()),
                ('pd_distance', models.IntegerField()),
                ('pd_weatherText', models.CharField(max_length=2000)),
                ('leakagePrediction', models.SmallIntegerField()),
                ('leakagePercentPrediction', models.DecimalField(decimal_places=2, max_digits=4)),
                ('UpdatedBy', models.CharField(max_length=30, null=True)),
                ('UpdatedOn', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 14, 4, 35, 866366), null=True),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='BillingDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 868304, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 868756, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 868360, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 868590, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 9, 8, 34, 35, 868268, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='predicteddata',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2018, 2, 9, 14, 4, 35, 868328), null=True),
        ),
    ]
