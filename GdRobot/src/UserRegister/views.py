#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from django.http.response import HttpResponse
from django.template import Template,Context
from _datetime import datetime
from django.template.loader import get_template
from django.template.loader import  get_template
import pymysql
from urllib.request import Request
from django.db import transaction 
from django.views.decorators.csrf import csrf_exempt
from django.db.migrations import graph
from django.contrib.sites import requests
from UserRegister.models import Member



# Create your views here.
@csrf_exempt
def index(request):
    # return HttpResponse(u"网站建设中...")
    GoLiveDay=datetime.strptime("2015-07-15 0:0:0","%Y-%m-%d %H:%M:%S")
    
    current_date=datetime.now()#获取当前时间
    day=(GoLiveDay-current_date).days
 
   
    hours=day*24
    second=hours*60
    print(day)
    print(GoLiveDay)
    print(current_date)  
    return render_to_response('index.html',locals())
def current_datetime_template(request):#当前日期
    GoLiveDay=datetime.datetime(2015,7,15,0,0,0)
    current_date=datetime.now()#获取当前时间
    day=(GoLiveDay-current_date).days
    print(day)
    print(current_date)  
    #return render_to_response('current_datetime.html',{'current_date':now})
    return render_to_response('current_datetime.html',locals())
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
        
        #print("autoID:"+str(user[0])+"编号："+str(user[1])+'密码'+str(user[2])+'姓名：'+str(user[3]))
    
    
    #print("取出数据库中用户信息：\n")
    #print(name)
    #print("当前信息为"+autoID+userID+userpsd+name+sex+birthday+hometown+nation+party+
    #      photo+department+job+address+postcode+gradSchool+gradTime+major+isHealth+highestDegree+
    #     techTitle+email+phoneDepartment+phonePersonal+phoneHome+phoneFax+nowMajor+Speciality+workYear+
    #      Language+LanguageLevel+descriptionJob+descriptionWork+isVerify
    #      )
    cur.close()
    db.close()
   
    return render_to_response('userinfo.html',locals() )
def userinfoSubmit(request):
    return render_to_response('userinsert.html')
@csrf_exempt    
def userInsert(request):
    if request.method=="POST":
        userID=request.POST['userID']
        userPsd=request.POST['userPsd']
        name=request.POST['name']
        sex=request.POST['sex']
        #birthday=request.POST['birthday']
        birthday=request.POST.get('birthday')
        hometown=request.POST['hometown']
        nation=request.POST['nation']
        party=request.POST['party']
        photo=request.FILES['photo']
        department=request.POST['department']
        job=request.POST['job']
        address=request.POST['address']
        postcode=request.POST['postcode']
        gradSchool=request.POST['gradeschool']
        gradeTime=request.POST['gradeTime']
        major=request.POST['major']
        health=request.POST['health']
        highestDegree=request.POST['highestDegree']
        techTitle=request.POST['techTitle']
        email=request.POST['email']
        phone_depart=request.POST['phone_depart']
        phone_personal=request.POST['phone_personal']
        phone_home=request.POST['phone_home']
        phone_fax=request.POST['phone_fax']
        now_major=request.POST['now_major']
        speciality=request.POST['speciality']
        workyear=request.POST['workyear']
        language=request.POST['language']
        language_level=request.POST['language_level']
        Descrition_job=request.POST['Description_job']
        Description_works=request.POST['Description_works']
        print(userID+userPsd+name+sex+email)
        member=Member(userid=userID,userpsd=userPsd,name=name,sex=sex,birthday=birthday,
                      hometown=hometown,nation=nation,party=party,photo=photo,department=department,
                      job=job,address=address,postcode=postcode,gradschool=gradSchool,gradtime=gradeTime,
                      major=major,health=health,highestdegree=highestDegree,techtitle=techTitle,email=email,
                      phone_depart=phone_depart,phone_personal=phone_personal,phone_home=phone_home,phone_fax=phone_fax,
                      now_major=now_major,speciality=speciality,workyears=workyear,language=language,language_level=language_level,
                      description_job=Descrition_job,description_works=Description_works,
                      )
        member.save()
    else:
               
        userID=request.GET['userID']
        userPsd=request.GET['userPsd']
        name=request.GET['name']
        sex=request.GET['sex']
        birthday=request.GET['birthday']
        hometown=request.GET['hometown']
        nation=request.GET['nation']
        party=request.GET['party']
        #photo=request.FILES['photo']
        department=request.GET['department']
        job=request.GET['job']
        address=request.GET['address']
        postcode=request.GET['postcode']
        gradSchool=request.GET['gradeschool']
        gradeTime=request.GET['gradeTime']
        major=request.GET['major']
        health=request.GET['health']
        highestDegree=request.GET['highestDegree']
        techTitle=request.GET['techTitle']
        email=request.GET['email']
        phone_depart=request.GET['phone_depart']
        phone_personal=request.GET['phone_personal']
        phone_home=request.GET['phone_home']
        phone_fax=request.GET['phone_fax']
        now_major=request.GET['now_major']
        speciality=request.GET['speciality']
        workyear=request.GET['workyear']
        language=request.GET['language']
        language_level=request.GET['language_level']
        Descrition_job=request.GET['Description_job']
        Description_works=request.GET['Description_works']
    #print(userID+userPsd+name+sex+birthday+hometown+nation+party+department+job+address+postcode+gradSchool+\
     #     gradeTime+major+health+highestDegree+techTitle+email+phone_depart+phone_personal+\
      #    phone_home+phone_fax+now_major+speciality+workyear+language+language_level+Descrition_job+Description_works)
    #db=pymysql.connect(user='root',db='robotdb',passwd='mysqladmin',host='localhost', charset='utf8')
    #print("数据库连接")
    #db.autocommit(True)
    #cur=db.cursor()
    #数据库插入，总共有32个字段，但是除去自增长autoID,isVertify之后有30个
   
    # sql="insert into member (userID,userPsd,name,sex) values ('0006','0006','张旭曼','女')"
    #cur.execute(sql)
   
    print("插入表单数据")
    #数据没有插入到数据中
    #cur.execute("INSERT INTO `member` (`userID`, `userPsd`, `name`, `sex`, `birthday`, \
    #`hometown`, `nation`, `party`, `department`, `job`, `address`, `postcode`, `gradSchool`, \
    #`gradTime`, `major`, `health`, `highestDegree`, `techTitle`, `email`, `phone_depart`, \
    #`phone_personal`, `phone_home`, `phone_fax`, `now_major`, `speciality`, `workYears`, \
    #`language`, `language_level`, `Description_job`, `Description_works`) \
    #VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
    #%s,%s,%s,%s,%s,%s)",[userID,userPsd,name,sex,birthday,hometown,nation,party,department,\
     #                    job,address,postcode,gradSchool,gradeTime,major,health,highestDegree,techTitle,\
      #                   email,phone_depart,phone_personal,phone_home,phone_fax,\
       #                  now_major,speciality,workyear,language,language_level,Descrition_job,Description_works]
    #)
   
    
   # db.close()
    
    if 'userID' in request.POST:
        message="信息注册成功，请返回主页.请牢记您的编号："+request.POST['userID'] 
        print (request.POST['userID'])
    else:
        message="个人信息注册不成功"
    return HttpResponse(message)

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
    
    