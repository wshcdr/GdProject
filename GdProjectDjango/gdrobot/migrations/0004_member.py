# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdrobot', '0003_auto_20150516_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('autoid', models.AutoField(primary_key=True, db_column='autoID', serialize=False)),
                ('userid', models.CharField(max_length=64, db_column='userID')),
                ('userpsd', models.CharField(max_length=64, db_column='userPsd')),
                ('name', models.CharField(max_length=16)),
                ('sex', models.CharField(max_length=16, null=True, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('hometown', models.CharField(max_length=64, null=True, blank=True)),
                ('nation', models.CharField(max_length=64, null=True, blank=True)),
                ('party', models.CharField(max_length=64, null=True, blank=True)),
                ('photo', models.FileField(upload_to='personalupload/')),
                ('department', models.CharField(max_length=64)),
                ('job', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('postcode', models.IntegerField()),
                ('gradschool', models.CharField(max_length=64, db_column='gradSchool')),
                ('gradtime', models.DateField(db_column='gradTime')),
                ('major', models.CharField(max_length=64)),
                ('health', models.CharField(max_length=64, null=True, blank=True)),
                ('highestdegree', models.CharField(max_length=64, db_column='highestDegree')),
                ('techtitle', models.CharField(max_length=64, db_column='techTitle', null=True, blank=True)),
                ('email', models.CharField(max_length=64)),
                ('phone_depart', models.IntegerField(null=True, blank=True)),
                ('phone_personal', models.IntegerField()),
                ('phone_home', models.IntegerField(null=True, blank=True)),
                ('phone_fax', models.IntegerField(null=True, blank=True)),
                ('now_major', models.CharField(max_length=64)),
                ('speciality', models.CharField(max_length=64, null=True, blank=True)),
                ('workyears', models.IntegerField(db_column='workYears', null=True, blank=True)),
                ('language', models.CharField(max_length=64, null=True, blank=True)),
                ('language_level', models.CharField(max_length=64, null=True, blank=True)),
                ('description_job', models.CharField(max_length=255, db_column='Description_job', null=True, blank=True)),
                ('description_works', models.CharField(max_length=255, db_column='Description_works', null=True, blank=True)),
                ('isverify', models.IntegerField(db_column='isVerify', null=True, blank=True)),
            ],
        ),
    ]
