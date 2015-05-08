from django.conf.urls import include, url
from django.contrib import admin
from UserRegister.views import index, userinfo ,userinfoSubmit,userInsert,userValidate,\
    userinsertBypost
from UserRegister.views import current_datetime_template
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'GdRobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),#��¼��ʾҳ
    url(r'^hello/$', current_datetime_template),#ģ��ҳ����ʾ���ǵ�ǰʱ��
    
    url(r'^userinfoSubmit/$', userinfoSubmit),
    url(r'^userInsert/$', userInsert),
    url(r'^userinfo/$', userinfo),
    url(r'^uservalidate/$', userValidate),
     url(r'^userInsertBypost/$', userinsertBypost),
    
]
