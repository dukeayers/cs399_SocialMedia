from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', splash),
    url(r'^dashboard/', dashboard),
    url(r'^logout/', logout_view),
	url(r'^new/', new_post),
	url(r'^signup/', signup),
	url(r'^about/', about),
    url(r'^admin/', include(admin.site.urls)),
)
