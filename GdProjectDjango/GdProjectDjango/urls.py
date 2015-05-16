from django.conf.urls import include, url
from django.contrib import admin
from gdrobot.views import index
urlpatterns = [
    # Examples:
    # url(r'^$', 'GdProjectDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^registerpage/', include('gdrobot.gdroboturls')),
    url(r'^admin/', include(admin.site.urls)),
]
