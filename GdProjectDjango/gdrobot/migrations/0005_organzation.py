# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdrobot', '0004_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organzation',
            fields=[
                ('autoid', models.AutoField(db_column='autoID', serialize=False, primary_key=True)),
                ('orgid', models.IntegerField(db_column='orgID')),
                ('orgpsd', models.CharField(db_column='orgPsd', max_length=45)),
                ('orgname', models.CharField(db_column='orgName', max_length=45)),
                ('orgcontact', models.CharField(db_column='orgContact', max_length=45)),
                ('orgphone', models.CharField(db_column='orgPhone', max_length=45)),
                ('orgfax', models.CharField(db_column='orgFax', null=True, blank=True, max_length=45)),
                ('orgaddress', models.CharField(db_column='orgAddress', null=True, blank=True, max_length=45)),
                ('orgpostcode', models.CharField(db_column='orgPostcode', null=True, blank=True, max_length=45)),
                ('orgemail', models.CharField(db_column='orgEmail', null=True, blank=True, max_length=45)),
                ('orglrname', models.CharField(db_column='orgLRName', null=True, blank=True, max_length=45)),
                ('orglrbirthday', models.DateField(db_column='orgLRBirthday', blank=True, null=True)),
                ('orglrtitle', models.CharField(db_column='orgLRTitle', null=True, blank=True, max_length=45)),
                ('orglreducation', models.CharField(db_column='orgLREducation', null=True, blank=True, max_length=45)),
                ('orglrphone', models.CharField(db_column='orgLRPhone', null=True, blank=True, max_length=45)),
                ('orglrhomephone', models.CharField(db_column='orgLRHomephoe', null=True, blank=True, max_length=45)),
                ('orglremail', models.CharField(db_column='orgLREmail', null=True, blank=True, max_length=45)),
                ('orgrname', models.CharField(db_column='orgRName', null=True, blank=True, max_length=45)),
                ('orgrbirthday', models.CharField(db_column='orgRBirthday', null=True, blank=True, max_length=45)),
                ('orgrtitle', models.CharField(db_column='orgRTitle', null=True, blank=True, max_length=45)),
                ('orgreducation', models.CharField(db_column='orgREducation', null=True, blank=True, max_length=45)),
                ('orgrphone', models.CharField(db_column='orgRPhone', null=True, blank=True, max_length=45)),
                ('orgrhomephone', models.CharField(db_column='orgRHomephoe', null=True, blank=True, max_length=45)),
                ('orgremail', models.CharField(db_column='orgREmail', null=True, blank=True, max_length=45)),
                ('orgresume', models.FileField(upload_to='orgupload/')),
                ('orgdetail', models.TextField(db_column='orgDetail', blank=True, null=True)),
                ('establishtime', models.DateField(db_column='establishTime', blank=True, null=True)),
                ('totalworkers', models.IntegerField(db_column='totalWorkers', blank=True, null=True)),
                ('techworkers', models.IntegerField(db_column='techWorkers', blank=True, null=True)),
                ('hightitle', models.IntegerField(blank=True, null=True)),
                ('midletitle', models.IntegerField(blank=True, null=True)),
                ('revenueoneyearago', models.IntegerField(db_column='revenueOneyearAgo', blank=True, null=True)),
                ('revenuetwoyearago', models.IntegerField(db_column='revenueTwoyearAgo', blank=True, null=True)),
                ('revenuethreeyearago', models.IntegerField(db_column='revenueThreeyearAgo', blank=True, null=True)),
                ('mainproduct', models.CharField(db_column='mainProduct', null=True, blank=True, max_length=255)),
                ('wanttitle', models.CharField(db_column='wantTitle', null=True, blank=True, max_length=255)),
                ('isagree', models.CharField(db_column='isAgree', null=True, blank=True, max_length=45)),
                ('isverfity', models.CharField(db_column='isVerfity', null=True, blank=True, max_length=45)),
            ],
        ),
    ]
