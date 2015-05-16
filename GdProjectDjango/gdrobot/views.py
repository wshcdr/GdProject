#encoding=utf8
# Create your views here.

import pymysql
from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.db import models
from django.db import models
from django.db import models
from gdrobot.models import Member,Organzation
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt 
def index(request):
    return render_to_response('indexhome.html')
@csrf_exempt 
def indexResigter(request):
    return render_to_response('index.html')
@csrf_exempt 
def Resigter(request):
    return render_to_response('register.html')
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
    
   
    #print("���������")
    
   
 
    if 'userID' in request.POST:
        message="注册成功，请牢记你的注册帐号"+request.POST['userID'] 
        print (request.POST['userID'])
    else:
        message="注册失败！！！请返回重新注册"
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

def userinfoSubmit(request):
    return render_to_response('userinsert.html')

def userValidate(request):
    db=pymysql.connect(user='root',db='robotdb',passwd='mysqladmin',host='localhost', charset='utf8')
    #print("���ݿ�����")
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
        print("���ݹ�������post����")
        userid1=request.POST['userID1']
        #userid2=request.POST.getUserData('userID1')
        userid2=request.POST.get('userID1')
        print("�û������idΪ")
        print(userid1+"get�����õ�"+userid2)
    
    
    
        
    return HttpResponse("HELLO WOLRD")
    

def userinfo(request):
    db=pymysql.connect(user='root',db='robotdb',passwd='mysqladmin',host='localhost', charset='utf8')
    #print("���ݿ�����")
    cur=db.cursor()
    cur.execute('select *from member order by autoID')
    userdata=cur.fetchall()
    for user in userdata:
        autoID=user[0]#������ID autoid
        userID=user[1]#�û���� userid
        userpsd=user[2] #�û����� userpsw
        name=user[3] #�û����� name
        sex=user[4] #�Ա� sex
        birthday=user[5]#����  birthday
        hometown=user[6] #���� hometown
        nation=user[7] #���� nation
        party=user[8] #���� Party
        photo=user[9] #��Ƭ photo
        department=user[10]#���� department
        job=user[11] #���� job
        address=user[12] #��ַ address
        postcode=user[13] #�ʱ� postcode
        gradSchool=user[14] #��ҵѧУ��gradSchool
        gradTime=user[15] #��ҵʱ�� gradtime
        major=user[16]#רҵ major
        isHealth=user[17]#����״�� health
        highestDegree=user[18]#���ѧ�� highestDegree
        techTitle=user[19] #ְ�� techTitle
        email=user[20] #���� Email
        phoneDepartment=user[21] #���ŵ绰 phone_department
        phonePersonal=user[22] #��ϵ�˵绰 phone_personal
        phoneHome=user[23] #��ͥ�绰 phone_home
        phoneFax=user[24] #���� phone_fax
        nowMajor=user[25] #��ǰ���� now_major
        Speciality=user[26]#�س� speciality
        workYear=user[27]#�������� workyear
        Language=user[28]#���� language
        LanguageLevel=user[29] #���Լ��� language_level
        descriptionJob=user[30] #ְλ���� Description_job
        descriptionWork=user[31] #������������ Description_work
        isVerify=user[32] #�Ƿ���֤ͨ��
        
        
    cur.close()
    db.close()
   
    return render_to_response('userinfo.html',locals() )   

           
