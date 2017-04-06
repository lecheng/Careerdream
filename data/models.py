from django.db import models
from django.utils import timezone
import uuid,datetime

# Create your models here.
class User_Active(models.Model):
	#C端活跃度
	datetime = models.DateField(blank=True, null=True)
	day_active = models.IntegerField(blank=True, null=True)
	week_active = models.IntegerField(blank=True, null=True)
	month_active = models.IntegerField(blank=True, null=True)
	week_inactive = models.CharField(max_length=10, blank=True, null=True)

class DailyRecordManager(models.Manager):
	def create_record(self, time, r1):
		r = self.create(datetime=time)
		r.c_ratio = r1
		return r

class DailyRecord(models.Model):
	#用户留存率
	datetime = models.DateTimeField(blank=True, null=True)
	b_ratio = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	c_ratio = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

	objects = DailyRecordManager()

	def get_date(self):
		return "%i-%i-%i" % (self.datetime.year, self.datetime.month, self.datetime.day)

class DataReportManager(models.Manager):
	def create_record(self, time, v1, v2, v3, v4, v5, v6,v7,v8,v9):
		record = self.create(datetime=time)
		record.total_reg = v1
		record.b_user_reg = v2
		record.c_user_reg = v3
		record.distinct_application_user = v4
		record.total_application = v5
		record.total_job = v6
		record.company_ip = v7
		record.bi_ip = v8
		record.line_position = v9
		return record

class DataReport(models.Model):
	#日常报告
	datetime = models.DateTimeField(blank=True, null=True)
	total_reg = models.IntegerField(blank=True, null=True)
	b_user_reg = models.IntegerField(blank=True, null=True)
	c_user_reg = models.IntegerField(blank=True, null=True)
	distinct_application_user = models.IntegerField(blank=True, null=True)
	total_application = models.IntegerField(blank=True, null=True)
	total_job = models.IntegerField(blank=True, null=True)
	company_ip = models.IntegerField(blank = True,null = True, default = '0')
	b_ip = models.IntegerField(blank = True,null = True, default = '0')
	line_position = models.IntegerField(blank= True,null = True,default = 0)




	objects = DataReportManager()

	def get_date(self):
		return "%i-%i-%i" % (self.datetime.year, self.datetime.month, self.datetime.day)

	def get_time(self):
		hour = str(self.datetime.hour)
		if self.datetime.hour < 10:
			hour = '0' + hour
		minute = str(self.datetime.minute)
		if self.datetime.minute < 10:
			minute = '0' + minute
		return '%s:%s' % (hour, minute)



class DailyPosition(models.Model):
	# """B端反馈情况"""
	datetime = models.DateField(blank = True, null = True)#日期
	c_read = models.IntegerField(blank = True,null = True)#B端查看
	c_forward = models.IntegerField(blank = True, null = True)#B端转发
	c_mark =  models.IntegerField(blank = True,null = True, )#B端标记数量
	c_expire = models.IntegerField(blank = True,null = True, )#到期不匹配
	c_works = models.IntegerField(blank = True, null = True, )#工作/学历不匹配
	average_application = models.FloatField(blank=True,default='0')#每人平均投递数
	daily_refresh = models.IntegerField(blank = True, default = 0)#刷新职位
	b_down = models.IntegerField(blank = True, null = True,default = 0)#B端下载
	position_due = models.IntegerField(blank = True,null =True,default = 0)#职位到期
	date_aver = models.FloatField(blank = True,null = True,default = 0)#B端平均反馈时间
	match_total  = models.IntegerField(blank = True,null = True,default = 0)#不匹配总数
	position = models.IntegerField(blank = True,null = True)#当日职位到期


	def get_date(self):
		return "%i-%i-%i" % (self.datetime.year,self.datetime.month,self.datetime.day)

class CommentData(models.Model):
	# """评论数据情况"""
	company_id = models.CharField(blank = True,null = True,max_length=10)#公司id
	coname = models.CharField(blank = True,null = True,max_length=100)#公司名
	company_email = models.CharField(blank = True, null = True,max_length=100)#帐号
	datetime = models.DateField(blank = True,null = True)#日期
	score = models.IntegerField(blank = True,default = 0,null = True)#投递响应评分
	resume_rate = models.CharField(blank = True,null = True,max_length=10)#简历处理率 
	tucao_count = models.IntegerField(blank = True,default = 0,null = True)#吐槽数
	support_count = models.IntegerField(blank = True,default = 0,null = True)#点赞/支持数
	date_comment = models.IntegerField(blank = True,default = 0,null = True)#当日评论数
	total_comment = models.IntegerField(blank = True,default = 0,null = True)#累计评论
	user_count = models.IntegerField(blank = True,default = 0, null = True)#参与评论用户数
	
	def get_date(self):
		return "%i-%i-%i" % (self.datetime.year,self.datetime.month,self.datetime.day)

class DataReg(models.Model):
	# """注册量"""
	datetime = models.DateField(blank = True,null = True)#日期
	c_user_reg = models.IntegerField(blank=True, null=True)#C当日端注册量
	b_total = models.IntegerField(blank = True,null =True)#B端当日总量
	b_active_reg = models.IntegerField(blank = True, null =True)#主动B端
	b_passive_reg = models.IntegerField(blank = True,null = True)#被动B端
	c_reg_total = models.IntegerField(blank = True,null = True)#C端总注册量
	b_reg_total = models.IntegerField(blank = True,null = True)#B端总注册量
	b_active_total = models.IntegerField(blank = True, null = True)#主动B端总注册量
	b_passive_total = models.IntegerField(blank = True,null = True)#被动B端总注册量
	b_active_singin = models.IntegerField(blank = True, null = True) #被动注册主动登录
	b_account = models.IntegerField(blank = True,default = 0,null = True)#账户数（邮件）

	def get_date(self):
		return "%i-%i-%i" % (self.datetime.year,self.datetime.month,self.datetime.day)

class DataBactive(models.Model):
	# """B端活跃情况"""
	datetime = models.DateField(blank = True,null = True)#日期
	user_active = models.IntegerField(blank = True, null = True)#活跃用户数
	user_loss = models.IntegerField(blank = True, null =True)#流失用户数
	loss_rate = models.DecimalField(blank = True, null = True,max_digits = 5, decimal_places = 2)#流失率
	return_rate = models.IntegerField(blank = True, null =True)#回流数
	not_active = models.IntegerField(blank = True,null = True)#不活跃用户数量
	not_active_rate = models.DecimalField(blank = True, null = True,max_digits = 5, decimal_places = 2)#不活跃用户比率

	def get_date(self):
		return "%i-%i-%i" % (self.datetime.year,self.datetime.month,self.datetime.day)

class DataCactive(models.Model):
	# """C端活跃情况"""
	datetime = models.DateField(blank = True,null = True)
	user_active = models.IntegerField(blank = True, null = True)#活跃用户数
	user_loss = models.IntegerField(blank = True, null =True)#流失用户数
	loss_rate = models.DecimalField(blank = True, null = True,max_digits = 5, decimal_places = 2)#流失率
	return_rate = models.IntegerField(blank = True, null =True)#回流数
	not_active = models.IntegerField(blank = True,null = True)#不活跃用户数量
	not_active_rate = models.DecimalField(blank = True, null = True,max_digits = 5, decimal_places = 2)#不活跃用户比率

	def get_date(self):
		return "%i-%i-%i" % (self.datetime.year,self.datetime.month,self.datetime.day)

class DataResume(models.Model):
	# """简历投递情况"""
	datetime = models.DateField(blank = True,null = True)
	pos_aver = models.FloatField(blank = True,null =True)#职位平均被投递
	resume_total = models.IntegerField(blank = True,null = True)#简历投递总量
	new_delivery = models.IntegerField(blank = True, null =True)#新增投递量 
	c_delivery = models.FloatField(blank = True, null = True)#C端平均投递量

	def get_date(self):
		return "%i-%i-%i" % (self.datetime.year,self.datetime.month,self.datetime.day)

class DataPosition(models.Model):
	# """职位信息"""
	datetime = models.DateField(blank = True,null = True)
	position_total = models.IntegerField(blank = True, null = True)#总职位数量
	add_position = models.IntegerField(blank = True,null = True)#主动B端增加职位数量   
	aver_position = models.FloatField(blank =True,null = True)#主动B端平均发布职位数量
	loss_add = models.IntegerField(blank = True,null = True)#被动B端增加职位数量
	loss_aver = models.FloatField(blank = True, null =True)#被动B端平均发布职位

	def get_date(self):
		return "%i-%i-%i" % (self.datetime.year,self.datetime.month,self.datetime.day)

	
