from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from careerdream import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'careerdream.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/hunter/',include('hunter.urls')),
    url(r'^api/hr/',include('hr.urls')),
    url(r'^api/phone/',include('mobile.urls')),
    url(r'^data/',include('data.urls')),
    url(r'^api/admin/', include(admin.site.urls)),
    url(r'^api/recommend/', include('recommend.urls')),
    url(r'^api/',include('main.urls')),
)
