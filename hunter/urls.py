from django.conf.urls import patterns, url

urlpatterns = patterns(
	'hunter.views',
	url('^initresumeinfo/$', 'initresumeinfo'),  				# 初始化在线简历
	url('^getresumeinfo/$', 'getresumeinfo'),  					# 获取在线简历信息
	url('^delete_resume/$', 'delete_resume'), 					# 删除附件简历
	url('^editresumeinfo/$', 'editresumeinfo'),  				# 编辑在线简历
	url('^change_default_resume/$', 'change_default_resume'),  	# 修改默认附件简历
	url('^uploadresume/$', 'uploadresume'),  					# 上传附件简历
	url('^deliver_resume/$', 'deliver_resume'),  				# 投递简历
	url('^delivery_list/$', 'delivery_list'),  					# 投递列表
	url('^leave_word/$', 'leave_word'),  						# 给公司发一段话
	url('^company_job_detail/$', 'company_job_detail'),

	url('^init_online_resume$', 'init_online_resume'),			# 初始化在线简历
	url('^edit_online_resume$', 'edit_online_resume'),			# 编辑在线简历
	url('^get_user_info$', 'get_user_info'),					# 获取用户信息
	url('^upload_avatar$', 'upload_avatar'),					# 上传头像
	url('^upload_resume$', 'upload_resume'),					# 上传简历
	url('^change_default_resume1$', 'change_default_resume1'),  # 修改默认简历
	url('^delete_resume1$', 'delete_resume1'),					# 删除简历
	url('^deliver_resume1$', 'deliver_resume1'),				# 投递简历
	url('^leave_word1$', 'leave_word1'),						# 投递简历
	url('^my_deliver$', 'my_deliver'),							# 我的投递
	url('^interview_message$', 'interview_message'),			# 面试信息
	url('^interview_user_feedback$', 'interview_user_feedback'),	# 面试反馈
)
