from django.conf.urls import include,url
from django.contrib import admin
from UserRegister.views import index, userinfo ,userinfoSubmit,userValidate,userinsertBypost
from UserRegister.registerviews import userInsert,organzationInsert,organzationSubmit
from django.conf import settings
from BackAdmin.views import userInfoAdmin

urlpatterns = [
    # Examples:
    # url(r'^$', 'GdRobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),#µÇÂ¼ÏÔÊ¾Ò³
    url(r'^register/', include('UserRegister.registerurls')),
    url(r'^background/', include('BackAdmin.Adminurls')),
    url(r'^robot/', include('WebContent.Contenturls')),
    
    
]
