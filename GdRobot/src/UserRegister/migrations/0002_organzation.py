# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserRegister', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organzation',
            fields=[
                ('autoid', models.AutoField(db_column='autoID', primary_key=True, serialize=False)),
                ('orgid', models.IntegerField(db_column='orgID')),
                ('orgpsd', models.CharField(db_column='orgPsd', max_length=45)),
                ('orgname', models.CharField(db_column='orgName', max_length=45)),
                ('orgcontact', models.CharField(db_column='orgContact', max_length=45)),
                ('orgphone', models.CharField(db_column='orgPhone', max_length=45)),
                ('orgfax', models.CharField(db_column='orgFax', null=True, max_length=45, blank=True)),
                ('orgaddress', models.CharField(db_column='orgAddress', null=True, max_length=45, blank=True)),
                ('orgpostcode', models.CharField(db_column='orgPostcode', null=True, max_length=45, blank=True)),
                ('orgemail', models.CharField(db_column='orgEmail', null=True, max_length=45, blank=True)),
                ('orglrname', models.CharField(db_column='orgLRName', null=True, max_length=45, blank=True)),
                ('orglrbirthday', models.DateField(db_column='orgLRBirthday', null=True, blank=True)),
                ('orglrtitle', models.CharField(db_column='orgLRTitle', null=True, max_length=45, blank=True)),
                ('orglreducation', models.CharField(db_column='orgLREducation', null=True, max_length=45, blank=True)),
                ('orglrphone', models.CharField(db_column='orgLRPhone', null=True, max_length=45, blank=True)),
                ('orglrhomephoe', models.CharField(db_column='orgLRHomephoe', null=True, max_length=45, blank=True)),
                ('orglremail', models.CharField(db_column='orgLREmail', null=True, max_length=45, blank=True)),
                ('orgrname', models.CharField(db_column='orgRName', null=True, max_length=45, blank=True)),
                ('orgrbirthday', models.CharField(db_column='orgRBirthday', null=True, max_length=45, blank=True)),
                ('orgrtitle', models.CharField(db_column='orgRTitle', null=True, max_length=45, blank=True)),
                ('orgreducation', models.CharField(db_column='orgREducation', null=True, max_length=45, blank=True)),
                ('orgrphone', models.CharField(db_column='orgRPhone', null=True, max_length=45, blank=True)),
                ('orgrhomephoe', models.CharField(db_column='orgRHomephoe', null=True, max_length=45, blank=True)),
                ('orgremail', models.CharField(db_column='orgREmail', null=True, max_length=45, blank=True)),
                ('orgresume', models.FileField(upload_to='orgupload/')),
                ('orgdetail', models.TextField(db_column='orgDetail', null=True, blank=True)),
                ('establishtime', models.DateField(db_column='establishTime', null=True, blank=True)),
                ('totalworkers', models.IntegerField(db_column='totalWorkers', null=True, blank=True)),
                ('techworkers', models.IntegerField(db_column='techWorkers', null=True, blank=True)),
                ('hightitle', models.IntegerField(null=True, blank=True)),
                ('midletitle', models.IntegerField(null=True, blank=True)),
                ('revenueOneyearAgo', models.IntegerField(null=True, blank=True)),
                ('revenueTwoyearAgo', models.IntegerField(null=True, blank=True)),
                ('revenueThreeyearAgo', models.IntegerField(null=True, blank=True)),
                ('mainproduct', models.CharField(db_column='mainProduct', null=True, max_length=255, blank=True)),
                ('wanttitle', models.CharField(db_column='wantTitle', null=True, max_length=255, blank=True)),
                ('isagree', models.CharField(db_column='isAgree', null=True, max_length=45, blank=True)),
                ('isverfity', models.CharField(db_column='isVerfity', null=True, max_length=45, blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'organzation',
            },
        ),
    ]
