from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.contrib import admin
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

class Member(models.Model):
    autoid = models.AutoField(db_column='autoID', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userID', max_length=64)  # Field name made lowercase.
    userpsd = models.CharField(db_column='userPsd', max_length=64)  # Field name made lowercase.
    name = models.CharField(max_length=16)
    sex = models.CharField(max_length=16, blank=True, null=True)
    birthday =  models.DateField(blank=True, null=True)
    hometown = models.CharField(max_length=64, blank=True, null=True)
    nation = models.CharField(max_length=64, blank=True, null=True)
    party = models.CharField(max_length=64, blank=True, null=True)
    photo=models.FileField(upload_to='personalupload/')
    #photo = models.CharField(max_length=64, blank=True, null=True)
    department = models.CharField(max_length=64)
    job = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    postcode = models.IntegerField()
    gradschool = models.CharField(db_column='gradSchool', max_length=64)  # Field name made lowercase.
    gradtime = models.DateField(db_column='gradTime')  # Field name made lowercase.
    major = models.CharField(max_length=64)
    health = models.CharField(max_length=64, blank=True, null=True)
    highestdegree = models.CharField(db_column='highestDegree', max_length=64)  # Field name made lowercase.
    techtitle = models.CharField(db_column='techTitle', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=64)
    phone_depart = models.IntegerField(blank=True, null=True)
    phone_personal = models.IntegerField()
    phone_home = models.IntegerField(blank=True, null=True)
    phone_fax = models.IntegerField(blank=True, null=True)
    now_major = models.CharField(max_length=64)
    speciality = models.CharField(max_length=64, blank=True, null=True)
    workyears = models.IntegerField(db_column='workYears', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(max_length=64, blank=True, null=True)
    language_level = models.CharField(max_length=64, blank=True, null=True)
    description_job = models.CharField(db_column='Description_job', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description_works = models.CharField(db_column='Description_works', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isverify = models.IntegerField(db_column='isVerify', blank=True, null=True)  # Field name made lowercase.

class Organzation(models.Model):
    autoid = models.AutoField(db_column='autoID', primary_key=True)  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID')  # Field name made lowercase.
    orgpsd = models.CharField(db_column='orgPsd', max_length=45)  # Field name made lowercase.
    orgname = models.CharField(db_column='orgName', max_length=45)  # Field name made lowercase.
    orgcontact = models.CharField(db_column='orgContact', max_length=45)  # Field name made lowercase.
    orgphone = models.CharField(db_column='orgPhone', max_length=45)  # Field name made lowercase.
    orgfax = models.CharField(db_column='orgFax', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgaddress = models.CharField(db_column='orgAddress', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgpostcode = models.CharField(db_column='orgPostcode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgemail = models.CharField(db_column='orgEmail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orglrname = models.CharField(db_column='orgLRName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orglrbirthday = models.DateField(db_column='orgLRBirthday', blank=True, null=True)  # Field name made lowercase.
    orglrtitle = models.CharField(db_column='orgLRTitle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orglreducation = models.CharField(db_column='orgLREducation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orglrphone = models.CharField(db_column='orgLRPhone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orglrhomephone = models.CharField(db_column='orgLRHomephoe', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orglremail = models.CharField(db_column='orgLREmail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgrname = models.CharField(db_column='orgRName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgrbirthday = models.CharField(db_column='orgRBirthday', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgrtitle = models.CharField(db_column='orgRTitle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgreducation = models.CharField(db_column='orgREducation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgrphone = models.CharField(db_column='orgRPhone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgrhomephone = models.CharField(db_column='orgRHomephoe', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgremail = models.CharField(db_column='orgREmail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orgresume = models.FileField(upload_to='orgupload/')  # Field name made lowercase.
    orgdetail = models.TextField(db_column='orgDetail', blank=True, null=True)  # Field name made lowercase.
    establishtime = models.DateField(db_column='establishTime', blank=True, null=True)  # Field name made lowercase.
    totalworkers = models.IntegerField(db_column='totalWorkers', blank=True, null=True)  # Field name made lowercase.
    techworkers = models.IntegerField(db_column='techWorkers', blank=True, null=True)  # Field name made lowercase.
    hightitle = models.IntegerField(blank=True, null=True)
    midletitle = models.IntegerField(blank=True, null=True)
    revenueoneyearago = models.IntegerField(db_column='revenueOneyearAgo', blank=True, null=True)  # Field name made lowercase.
    revenuetwoyearago = models.IntegerField(db_column='revenueTwoyearAgo', blank=True, null=True)  # Field name made lowercase.
    revenuethreeyearago = models.IntegerField(db_column='revenueThreeyearAgo', blank=True, null=True)  # Field name made lowercase.
    mainproduct = models.CharField(db_column='mainProduct', max_length=255, blank=True, null=True)  # Field name made lowercase.eld name made lowercase.
    wanttitle = models.CharField(db_column='wantTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isagree = models.CharField(db_column='isAgree', max_length=45, blank=True, null=True)  # Field name made lowercase.
    isverfity = models.CharField(db_column='isVerfity', max_length=45, blank=True, null=True)  # Field name made lowercase.

admin.site.register(Member)
admin.site.register(Organzation)
