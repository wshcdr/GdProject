# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('autoid', models.AutoField(primary_key=True, db_column='autoID', serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'admin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('autoid', models.AutoField(primary_key=True, db_column='autoID', serialize=False)),
                ('userid', models.CharField(db_column='userID', max_length=64)),
                ('userpsd', models.CharField(db_column='userPsd', max_length=64)),
                ('name', models.CharField(max_length=16)),
                ('sex', models.CharField(blank=True, null=True, max_length=16)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('hometown', models.CharField(blank=True, null=True, max_length=64)),
                ('nation', models.CharField(blank=True, null=True, max_length=64)),
                ('party', models.CharField(blank=True, null=True, max_length=64)),
                ('photo', models.FileField(upload_to='personalupload/')),
                ('department', models.CharField(max_length=64)),
                ('job', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('postcode', models.IntegerField()),
                ('gradschool', models.CharField(db_column='gradSchool', max_length=64)),
                ('gradtime', models.DateField(db_column='gradTime')),
                ('major', models.CharField(max_length=64)),
                ('health', models.CharField(blank=True, null=True, max_length=64)),
                ('highestdegree', models.CharField(db_column='highestDegree', max_length=64)),
                ('techtitle', models.CharField(blank=True, null=True, db_column='techTitle', max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('phone_depart', models.IntegerField(blank=True, null=True)),
                ('phone_personal', models.IntegerField()),
                ('phone_home', models.IntegerField(blank=True, null=True)),
                ('phone_fax', models.IntegerField(blank=True, null=True)),
                ('now_major', models.CharField(max_length=64)),
                ('speciality', models.CharField(blank=True, null=True, max_length=64)),
                ('workyears', models.IntegerField(blank=True, null=True, db_column='workYears')),
                ('language', models.CharField(blank=True, null=True, max_length=64)),
                ('language_level', models.CharField(blank=True, null=True, max_length=64)),
                ('description_job', models.CharField(blank=True, null=True, db_column='Description_job', max_length=255)),
                ('description_works', models.CharField(blank=True, null=True, db_column='Description_works', max_length=255)),
                ('isverify', models.IntegerField(blank=True, null=True, db_column='isVerify')),
            ],
            options={
                'db_table': 'member',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('autoid', models.IntegerField(primary_key=True, db_column='autoID', serialize=False)),
                ('memberid', models.IntegerField(db_column='memberID')),
                ('units', models.CharField(max_length=64)),
                ('contact', models.CharField(max_length=64)),
                ('tel', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('address', models.CharField(max_length=64)),
                ('zipcode', models.IntegerField(db_column='zipCode')),
                ('email', models.CharField(max_length=64)),
                ('lealperson', models.CharField(db_column='lealPerson', max_length=16)),
                ('delegate', models.CharField(max_length=16)),
                ('delegate_resume', models.TextField()),
                ('units_situation', models.CharField(blank=True, null=True, max_length=64)),
                ('units_time', models.DateTimeField(blank=True, null=True)),
                ('units_count', models.IntegerField(blank=True, null=True)),
                ('units_tech', models.IntegerField(blank=True, null=True)),
                ('units_hightitle', models.IntegerField(blank=True, null=True, db_column='units_highTitle')),
                ('units_midtitle', models.IntegerField(blank=True, null=True, db_column='units_midTitle')),
                ('units_turnover1', models.IntegerField(blank=True, null=True)),
                ('units_turnover2', models.IntegerField(blank=True, null=True)),
                ('units_turnover3', models.IntegerField(blank=True, null=True)),
                ('mainproduct', models.CharField(blank=True, null=True, db_column='mainProduct', max_length=255)),
                ('intention', models.CharField(blank=True, null=True, max_length=64)),
                ('unitscomments', models.CharField(blank=True, null=True, db_column='unitsComments', max_length=64)),
                ('isok', models.CharField(blank=True, null=True, db_column='isOK', max_length=64)),
            ],
            options={
                'db_table': 'register',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=50)),
                ('UploadFiles', models.FileField(upload_to='./upload/')),
            ],
        ),
    ]
