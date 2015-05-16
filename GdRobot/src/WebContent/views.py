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
    return render_to_response('indexhome.html')
