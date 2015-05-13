#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from django.http.response import HttpResponse
from django.template import Template,Context
from datetime import datetime
from django.template.loader import get_template
from django.template.loader import  get_template
import pymysql
from django.db import transaction 
from django.views.decorators.csrf import csrf_exempt
from django.db.migrations import graph
from django.contrib.sites import requests
from UserRegister.models import Organzation,Member

@csrf_exempt    
def userInsert(request):
    if request.method=="POST":
        userID=request.POST['userID']
        userPsd=request.POST['userPsd']
        name=request.POST['name']
        sex=request.POST['sex']
        birthday=request.POST['birthday']
        #birthday=request.POST.get('birthday',1970-01-01)
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
    
   
    print("插入表单数据")
    
   
 
    if 'userID' in request.POST:
        message="信息注册成功，请返回主页.请牢记您的编号："+request.POST['userID'] 
        print (request.POST['userID'])
    else:
        message="个人信息注册不成功"
    return HttpResponse(message)

def organzationSubmit(request):
    print("hello world")
    return  render_to_response('Departmentinsert.html', locals())
@csrf_exempt
def organzationInsert(request):
    if request.method=="POST":
        orgID=request.POST['orgID']
        orgPsd=request.POST['orgPsd']
        orgName=request.POST['orgname']
        orgContact=request.POST['orgContact']
        orgPhone=request.POST['orgphone']
        orgFax=request.POST['orgfax']
        orgAddress=request.POST['orgaddress']
        orgPostcode=request.POST['orgpostcode']
        orgEmail=request.POST['orgemail']
        orgLrname=request.POST['lRname']
        orgLrbirthday=request.POST['lRbirthday']
        orgLrtitle=request.POST['lRtitle']
        orgLreducation=request.POST['lReducation']
        orgLrphone=request.POST['lRphone']
        orgLrhomephone=request.POST['lRhomephone']
        orgLremail=request.POST['lRemail']
        orgRname=request.POST['orgRname']
        orgRbirthday=request.POST['orgRBirthday']
        orgRtitle=request.POST['orgRtitle']
        orgReducation=request.POST['orgReducation']
        orgRphone=request.POST['orgRphone']
        orgRhomephone=request.POST['orgRhomephone']
        orgRemail=request.POST['orgRemail']
        orgResume=request.FILES['resume']
        orgDetail=request.POST['orgdetails']
        Establishtime=request.POST['establishTime']
        Totalworkers=request.POST['totalworkers']
        Techwokers=request.POST['techworks']
        Hightitle=request.POST['highTitle']
        Midletitle=request.POST['midleTitle']
        RevenueLast=request.POST['Revenue14']
        RevenueBeforelaost=request.POST['Revenue13']
        RevenueThree=request.POST['Revenue12']
        MainProduct=request.POST['mainProduct']
        Wanttitle=request.POST['wantTitle']
        print(orgID+orgPsd+orgName+orgAddress+orgContact+orgDetail+orgEmail+orgRtitle+orgRphone+orgRhomephone
              +orgLrbirthday+orgLremail+orgLrname+orgPostcode+orgRbirthday+orgReducation)
   
        organzation=Organzation(orgid=orgID,orgpsd=orgPsd,orgname=orgName,orgcontact=orgContact,
                                orgphone=orgPhone,orgfax=orgFax,orgaddress=orgAddress,orgpostcode=orgPostcode,
                                orgemail=orgEmail,orglrname=orgLrname,orglrbirthday=orgLrbirthday,
                                orglrtitle=orgLrtitle,orglreducation=orgLreducation,orglrphone=orgLrphone,
                                orglrhomephone=orgLrhomephone,
                                orglremail=orgLremail,orgrname=orgRname,
                                orgrbirthday=orgRbirthday,orgrtitle=orgRtitle,orgreducation=orgReducation,
                                orgrphone=orgRphone,
                                orgrhomephone=orgRhomephone,
                                orgremail=orgRemail,
                                orgresume=orgResume,orgdetail=orgDetail,establishtime=Establishtime,
                                totalworkers=Totalworkers,techworkers=Techwokers,hightitle=Hightitle,
                                midletitle=Midletitle,revenueoneyearago=RevenueLast,revenuetwoyearago=RevenueBeforelaost,
                                revenuethreeyearago=RevenueThree,mainproduct=MainProduct,wanttitle=Wanttitle,
                                )
        organzation.save()
    return HttpResponse("hello world")
           