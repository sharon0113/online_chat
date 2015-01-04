from django.conf.urls import patterns, include, url
from chat.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kefu.views.home', name='home'),
    # url(r'^kefu/', include('kefu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	url(r'^chat/$',chat),
	url(r'^teacher/$',chat_server),
	url(r'^login/$',login),
	url(r'^sendMsg/$',sendMsg),
	url(r'^getNewMsg/$',getNewMsg),
	url(r'^getclientlist/$',getclientlist),
	url(r'^hide/$',hide),
	url(r'^getmax/$',getmax),
	url(r'^open_mark/',mark),
	url(r'^getoldmsg/$',getoldmsg),
	url(r'^logout/$',logout),
	url(r'^query/$',query),
	url(r'^getlog/$',getlog),
)
