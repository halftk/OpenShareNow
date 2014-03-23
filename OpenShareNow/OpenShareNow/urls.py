from django.conf.urls import patterns, include, url

from osnow.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OpenShareNow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', mainpage, name='home'),
	url(r'^user/(\w+)/$', userpage),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$','django.contrib.auth.views.login'),
)
