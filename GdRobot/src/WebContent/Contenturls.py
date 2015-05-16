from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from WebContent.views import index
from django.utils.termcolors import background
urlpatterns = [
    # Examples:
    # url(r'^$', 'GdRobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/$', index),
    url(r'^home/$', index),
    
    
    
]