# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('role', models.CharField(choices=[('Prime_admin', 'Prime_Administrator'), ('Hospital_management', 'Hospital_Management'), ('Hospital_admin', 'Hospital_Administrator')], max_length=30, default='Prime_Administrator')),
                ('mobile', models.CharField(max_length=10)),
                ('office_contact', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
