# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeExchange', '0002_auto_20171021_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, help_text='Optional.')),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('postal_address', models.TextField(max_length=100, blank=True, null=True)),
                ('office_contact', models.IntegerField()),
                ('mobile_contact', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='user_data',
        ),
    ]
