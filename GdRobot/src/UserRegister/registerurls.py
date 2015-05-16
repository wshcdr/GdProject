from django.conf.urls import include, url
from django.contrib import admin
from UserRegister.views import  userinfo ,userinfoSubmit,userValidate,userinsertBypost

from django.conf import settings
from UserRegister.registerviews import organzationSubmit, organzationInsert,userInsert,index
urlpatterns = [
    # Examples:
    # url(r'^$', 'GdRobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^userinfoSubmit/$', userinfoSubmit),
    url(r'^userinfoSubmit/userInsert/$', userInsert),
    url(r'^userinfo/$', userinfo),
    url(r'^uservalidate/$', userValidate),
    #url(r'^userInsertBypost/$', userinsertBypost),
    #url(r'^userInsertBypost/$', userinsertBypost),
    url(r'^organzationinfoSubmit/$', organzationSubmit),
    url(r'^organzationinfoSubmit/organzationInsert/$', organzationInsert),
    
]
