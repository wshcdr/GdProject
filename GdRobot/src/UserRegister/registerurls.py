from django.conf.urls import include, url
from django.contrib import admin
from UserRegister.views import index, userinfo ,userinfoSubmit,userValidate,userinsertBypost

from django.conf import settings
from UserRegister.registerviews import organzationSubmit, organzationInsert,userInsert
urlpatterns = [
    # Examples:
    # url(r'^$', 'GdRobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^userinfoSubmit/$', userinfoSubmit),
    url(r'^userInsert/$', userInsert),
    url(r'^userinfo/$', userinfo),
    url(r'^uservalidate/$', userValidate),
    #url(r'^userInsertBypost/$', userinsertBypost),
    #url(r'^userInsertBypost/$', userinsertBypost),
    url(r'^organzationinfoSubmit/$', organzationSubmit),
    url(r'^organzationInsert/$', organzationInsert),
    
]
