from django.conf.urls import include, url
from django.contrib import admin
from gdrobot.views import userInsert,organzationInsert,organzationSubmit,userinfo,userInsert,userinfoSubmit,userValidate,Resigter
from django.conf import settings
from gdrobot.views import index,indexResigter
from django.utils.termcolors import background
urlpatterns = [
    # Examples:
    # url(r'^$', 'GdRobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', indexResigter),
    url(r'^register/$', Resigter),
    url(r'^userinfoSubmit/$', userinfoSubmit),
    url(r'^userinfoSubmit/userInsert/$', userInsert),
    url(r'^userinfo/$', userinfo),
    url(r'^uservalidate/$', userValidate),
    #url(r'^userInsertBypost/$', userinsertBypost),
    #url(r'^userInsertBypost/$', userinsertBypost),
    url(r'^organzationinfoSubmit/$', organzationSubmit),
    url(r'^organzationinfoSubmit/organzationInsert/$', organzationInsert),
    
]