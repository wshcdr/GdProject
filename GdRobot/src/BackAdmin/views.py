#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.db import models
from django.db import models
from django.db import models
from BackAdmin.models import Member,Organzation
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt 
def index(request):
    return render_to_response('adminPage.html')
    #return HttpResponse('后台管理')
@csrf_exempt 
def userInfoAdmin(request):
    if request.method=='POST':
        memberDetails=Member.objects.all()
        print(memberDetails)   
        return render_to_response('userinfoAdmin.html',locals())
    else:
        
        return render_to_response('errorPage.html')
@csrf_exempt  
def organzationAdmin(request):
    if request.method=='POST':
        organazationDetails=Organzation.objects.all()
        
        print(organazationDetails.count())
        return render_to_response('organzationinfoAdmin.html', locals())
    else:
        return render_to_response('errorPage.html')
def Log(request):
    pass
def SomeOperation(request):
    pass