from __future__ import unicode_literals
from django.db import models
from django.db import models
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



class Admin(models.Model):
    autoid = models.AutoField(db_column='autoID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'admin'


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
    photo = models.CharField(max_length=64, blank=True, null=True)
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

    class Meta:
        managed = True
        db_table = 'member'


class Register(models.Model):
    autoid = models.IntegerField(db_column='autoID', primary_key=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='memberID')  # Field name made lowercase.
    units = models.CharField(max_length=64)
    contact = models.CharField(max_length=64)
    tel = models.IntegerField()
    fax = models.IntegerField()
    address = models.CharField(max_length=64)
    zipcode = models.IntegerField(db_column='zipCode')  # Field name made lowercase.
    email = models.CharField(max_length=64)
    lealperson = models.CharField(db_column='lealPerson', max_length=16)  # Field name made lowercase.
    delegate = models.CharField(max_length=16)
    delegate_resume = models.TextField()
    units_situation = models.CharField(max_length=64, blank=True, null=True)
    units_time = models.DateTimeField(blank=True, null=True)
    units_count = models.IntegerField(blank=True, null=True)
    units_tech = models.IntegerField(blank=True, null=True)
    units_hightitle = models.IntegerField(db_column='units_highTitle', blank=True, null=True)  # Field name made lowercase.
    units_midtitle = models.IntegerField(db_column='units_midTitle', blank=True, null=True)  # Field name made lowercase.
    units_turnover1 = models.IntegerField(blank=True, null=True)
    units_turnover2 = models.IntegerField(blank=True, null=True)
    units_turnover3 = models.IntegerField(blank=True, null=True)
    mainproduct = models.CharField(db_column='mainProduct', max_length=255, blank=True, null=True)  # Field name made lowercase.
    intention = models.CharField(max_length=64, blank=True, null=True)
    unitscomments = models.CharField(db_column='unitsComments', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isok = models.CharField(db_column='isOK', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'register'
class UploadFiles(models.Model):
    username=models.CharField(max_length=50)
    UploadFiles=models.FileField(upload_to='./upload/')
    
