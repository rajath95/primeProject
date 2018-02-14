# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0007_auto_20180208_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictedData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('RecordID', models.IntegerField()),
                ('ClientID', models.CharField(max_length=30, default='gleneagles_lbn')),
                ('UHID', models.IntegerField()),
                ('AdmissionNumber', models.BigIntegerField(null=True, default=999)),
                ('RegistrationDate', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 8, 13, 16, 18, 743947, tzinfo=utc))),
                ('RegistrationNumber', models.BigIntegerField()),
                ('BillingDate', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 8, 13, 16, 18, 743984, tzinfo=utc))),
                ('BillingNumber', models.BigIntegerField()),
                ('TimeOfBilling', models.TimeField(verbose_name=datetime.datetime(2018, 2, 8, 18, 46, 18, 744009), null=True)),
                ('PatientZIP', models.IntegerField(null=True)),
                ('PatientDateOfBirth', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 8, 13, 16, 18, 744042, tzinfo=utc), null=True)),
                ('PatientGender', models.CharField(max_length=30, null=True)),
                ('PatientName', models.CharField(max_length=100, default='NA')),
                ('PatientContact', models.CharField(max_length=30, default='9999999999')),
                ('ServiceCode', models.CharField(max_length=30)),
                ('ServiceName', models.CharField(max_length=100)),
                ('NumberOfUnitsOfService', models.IntegerField()),
                ('ServiceAmount', models.DecimalField(max_digits=18, decimal_places=2, null=True)),
                ('DoctorName', models.CharField(max_length=100)),
                ('FinalBillAmount', models.DecimalField(max_digits=18, decimal_places=2, null=True)),
                ('FinalDiscountAmount', models.DecimalField(max_digits=18, decimal_places=2, null=True)),
                ('PaymentMode', models.CharField(max_length=30, null=True)),
                ('PaymentAmount', models.DecimalField(max_digits=18, decimal_places=2, null=True)),
                ('PaymentDate', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 8, 13, 16, 18, 744284, tzinfo=utc), null=True)),
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
                ('NextVisitDate', models.DateTimeField(verbose_name=datetime.datetime(2018, 2, 8, 13, 16, 18, 744451, tzinfo=utc), null=True)),
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
                ('leakagePercentPrediction', models.DecimalField(max_digits=4, decimal_places=2)),
                ('UpdatedBy', models.CharField(max_length=30, null=True)),
                ('UpdatedOn', models.DateTimeField(null=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='doctormaster',
            name='SMSConsentEndDate',
            field=models.DateTimeField(null=True, default=datetime.datetime(2018, 2, 7, 18, 46, 18, 742034)),
        ),
    ]
