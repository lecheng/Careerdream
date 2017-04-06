# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from careerdream import settings

urlpatterns = patterns('main.views',
	#页面跳转
	url(r'^$', 'home'),
	url(r'login/$','login'),
	#api
	url(r'list/$','index'),
	url(r'signin/$','signin'),
	url(r'signup/$','signup'),
	url(r'signout/$','signout'),
	url(r'findpwdemail/$','findpwdemail'),
	url(r'resetpwd/$','resetpwd'),
	url(r'updatepwd/$','updatepwd'),
	url(r'wechat/$','wechat'),
	url(r'bind/$','bind'),
	url('^upload_avatar/$', 'upload_avatar'),
	url('^save_avatar/$', 'save_avatar'),
	url('^uber_benefit/$', 'uber_benefit'),
	url('^category/$', 'category'),
	url('^article/$', 'article'),
	url('^uploadLogo/$', 'uploadLogo'),
	url('^saveLogo/$', 'saveLogo'),
	url(r'^addcomment/$','addcomment',name='addcomment'), 
    	url(r'^replay/$','replay',name='replay'),
   	url(r'^commentEnter/$','commentEnter'),
	url(r'^delet_comment','delet_comment',name='delet_comment'),
	url(r'commentDetail/$','commentDetail',name='commentDetail'),
	url(r'^companyTop/$','companyTop'),
)
urlpatterns += patterns('',
    url(r'^api/admin/', include(admin.site.urls)),  
)

