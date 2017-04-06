from django.conf.urls import patterns, url

urlpatterns = patterns(
	'hr.views',
	url('^hr_resume_manage/$', 'hr_resume_manage'),   			# 管理收到的简历
	url('^hr_reject_resume/$', 'hr_reject_resume'),   			# 标记简历状态为不合适
	url('^hr_forward_resume/$', 'hr_forward_resume'),  			# 标记简历状态为转发
	url('^hr_read_resume/$', 'hr_read_resume'),    				# 标记简历状态为已读

	url('^hr_interview_resume/$', 'hr_interview_resume'),    	# 约面试
	url('^hr_contacts_message/$', 'hr_contacts_message'),    	# 获取联系人信息
	url('^interview_hr_feedback', 'interview_hr_feedback'),	    # 面试反馈


	url('^hr_reduction_resume/$', 'hr_reduction_resume'),  		# 还原简历状态
	url('^edit_company_info/$', 'edit_company_info'),  			# 编辑公司信息
	url('^hr_job_manage/$', 'hr_job_manage'),    				# 职位管理
	url('^hr_get_job_info/$', 'hr_get_job_info'),   			# 获取职位信息
	url('^post_job/$', 'post_job'),    							# 发布新职位或编辑现有职位
	url('^get_job_info/$', 'get_job_info'),   					# 编辑现有职位时获取职位信息
	url('^resumeCategory/$', 'resumeCategory'),   				# 简历管理分类汇总
	url('^downresume/$', 'downresume'),   			            # 下载简历(pdf)
	url('^improper/$','improper'),						        # 不合适弹框
	url('^manageImproper/$','manageImproper'),

	url('^resume_manage$', 'resume_manage'),					# 简历管理
)
