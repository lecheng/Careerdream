# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('data.views',
                  url(r'^$', 'dataSignin'),
                   url(r'^signin/', 'dataSignin'),
                   url(r'^login/', 'dataLogin'),
                   #url(r'^datareport/$', 'dataAnalysisReport'),                                #数据统计页面
                   url(r'^jobrank/$','datajob'),
                   url(r'^newcompany/$','dataNewCompany'),
                   url(r'^updatedata/$', 'updateData'),
                   url(r'^creport/$','creport'),
                   url(r'^dataFeedback/$','dataFeedback'),#B端反馈情况
                  url(r'^commentdata/$','dataComment'),
                  url(r'^dataReg/$','dataReg'),# 注册量
                  url(r'^dataBactive/$','dataBactive'),# B端活跃情况
                  url(r'^dataCactive/$','dataCactive'),# C端活跃情况
                  url(r'^dataResume/$','dataResume'),# 简历投递情况
                  url(r'^dataPosition/$','dataPosition'),# 职位信息
                  url(r'^dataIndex/$','dataIndex')
)
