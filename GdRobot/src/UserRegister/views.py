#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from django.http.response import HttpResponse
from django.template import Template,Context
from _datetime import datetime, date
from django.template.loader import get_template
from django.template.loader import  get_template
import pymysql
from urllib.request import Request
from django.db import transaction 
from django.views.decorators.csrf import csrf_exempt
from django.db.migrations import graph
from django.contrib.sites import requests
from UserRegister.models import Member
from django.db.models.lookups import Second



# Create your views here.
@csrf_exempt
def index(request):
    # return HttpResponse(u"网站建设中...")
    GoLiveDay=datetime.strptime("2015-07-15 0:0:0","%Y-%m-%d %H:%M:%S")
    
    
    current_date=datetime.now()#获取当前时间
    
   
    day=(GoLiveDay-current_date).days
    test=(GoLiveDay-current_date)
    hours=day*24
    second=hours*60
    print(current_date)
    print(second)
    print(test)
    print(day)
    return render_to_response('index.html',locals())

def userinfo(request):
    db=pymysql.connect(user='root',db='robotdb',passwd='mysqladmin',host='localhost', charset='utf8')
    #print("数据库连接")
    cur=db.cursor()
    cur.execute('select *from member order by autoID')
    userdata=cur.fetchall()
    for user in userdata:
        autoID=user[0]#自增长ID autoid
        userID=user[1]#用户编号 userid
        userpsd=user[2] #用户密码 userpsw
        name=user[3] #用户姓名 name
        sex=user[4] #性别 sex
        birthday=user[5]#生日  birthday
        hometown=user[6] #籍贯 hometown
        nation=user[7] #国籍 nation
        party=user[8] #党派 Party
        photo=user[9] #相片 photo
        department=user[10]#部门 department
        job=user[11] #工作 job
        address=user[12] #地址 address
        postcode=user[13] #邮编 postcode
        gradSchool=user[14] #毕业学校，gradSchool
        gradTime=user[15] #毕业时间 gradtime
        major=user[16]#专业 major
        isHealth=user[17]#健康状况 health
        highestDegree=user[18]#最高学历 highestDegree
        techTitle=user[19] #职称 techTitle
        email=user[20] #邮箱 Email
        phoneDepartment=user[21] #部门电话 phone_department
        phonePersonal=user[22] #联系人电话 phone_personal
        phoneHome=user[23] #家庭电话 phone_home
        phoneFax=user[24] #传真 phone_fax
        nowMajor=user[25] #当前领域 now_major
        Speciality=user[26]#特长 speciality
        workYear=user[27]#工作年限 workyear
        Language=user[28]#语言 language
        LanguageLevel=user[29] #语言级别 language_level
        descriptionJob=user[30] #职位描述 Description_job
        descriptionWork=user[31] #所做工作描述 Description_work
        isVerify=user[32] #是否验证通过
        
        
    cur.close()
    db.close()
   
    return render_to_response('userinfo.html',locals() )
def userinfoSubmit(request):
    return render_to_response('userinsert.html')

def userValidate(request):
    db=pymysql.connect(user='root',db='robotdb',passwd='mysqladmin',host='localhost', charset='utf8')
    #print("数据库连接")
    cur=db.cursor()
    cur.execute('select *from member order by autoID')
    userdata=cur.fetchall()
    #for user in userdata:
    agree_1=request.GET.getlist('agree')
    print(agree_1)
    cur.close()
    db.close()
   
    return render_to_response('userValidate.html',locals() )
@csrf_exempt
def userinsertBypost(request):
    if request.method=="POST":
        print("传递过来的是post方法")
        userid1=request.POST['userID1']
        #userid2=request.POST.getUserData('userID1')
        userid2=request.POST.get('userID1')
        print("用户输入的id为")
        print(userid1+"get方法得到"+userid2)
    
    
    
        
    return HttpResponse("HELLO WOLRD")
    
    