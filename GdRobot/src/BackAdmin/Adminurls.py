from django.conf.urls import include, url
from django.contrib import admin
from BackAdmin.views import index
from django.conf import settings
from BackAdmin.views import userInfoAdmin,organzationAdmin,organzationAdminCheck
from django.utils.termcolors import background
urlpatterns = [
    # Examples:
    # url(r'^$', 'GdRobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/$', index),
    url(r'^userinfoadmin/$', userInfoAdmin),
    url(r'^organzationadmin/$', organzationAdmin),
    url(r'^organazationDetailsCheck/$', organzationAdminCheck),
    
    
]
