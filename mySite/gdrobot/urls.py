from django.conf.urls import *
from gdrobot.views import archive

urlpatterns = patterns('',
                      url(r'^$',archive),
                      )