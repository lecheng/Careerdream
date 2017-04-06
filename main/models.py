# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import uuid, datetime

# Create your models here.
def avatar_path(instance, filename):
	return '/'.join(['avatar', instance.id + '.' + filename.split('.')[-1]])


def introvideo_path(instance, filename):
	return '/'.join(['intro', instance.id + '.mp4'])


def resume_path(instance, filename):
	return '/'.join(['resume', str(instance.user.id),
					 filename[:filename.rfind('.')] + filename[filename.rfind('.'):]])


def logo_path(instance, filename):
	return '/'.join(['logo', instance.id + '.' + filename.split('.')[-1]])


def video_path(instance, filename):
	return '/'.join(['video', instance.application.user.id,
					 instance.application.job.id, instance.topic.id + '_' + filename])


def getApplicationTime(application):
	return application.time


class UserManager(models.Manager):
	def create_user(self, email, pwd):
		time = timezone.now()
		user = self.create(email=email, userpwd=pwd, register_date=time, last_login_date=time)
		return user

	def create_user_wechat(self, openid):
		time = timezone.now()
		user = self.create(wechat_openid=openid, register_date=time, last_login_date=time)
		curtime = datetime.datetime(time.year, time.month, time.day)
		return user


class User(models.Model):
	unique_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
	username = models.CharField(blank=True, max_length=50)
	userpwd = models.CharField(blank=True, max_length=80)
	email = models.EmailField(blank=True, max_length=50)
	gender_choices = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=gender_choices, default='M')
	wechat_openid = models.CharField(blank=True, max_length=50)
	wechat_informid = models.CharField(blank=True, max_length=50)
	phone = models.CharField(blank=True, max_length=20)
	city = models.CharField(blank=True, max_length=100)
	avatar = models.ImageField(blank=True, upload_to='avatar')
	# introvideo = models.FilePathField(path=introvideo_path)	
	school = models.CharField(blank=True, max_length=50)
	major = models.CharField(blank=True, max_length=50)
	degree_choices = (
		('J', 'Junior college'),
		('B', 'Bachelor'),
		('M', 'Master'),
		('P', 'PhD'),
	)
	degree = models.CharField(max_length=1, choices=degree_choices, default='B')
	gradyear = models.IntegerField(null=True, blank=True)
	is_activated = models.BooleanField(default=False)
	register_date = models.DateTimeField(blank=True, null=True)
	last_login_date = models.DateTimeField(blank=True, null=True)
	is_vip_user = models.BooleanField(default=False)
	review = models.TextField(blank=True, null=True)
	searched = models.TextField(blank=True, null=True)

	birth = models.DateField(blank=True, null=True, verbose_name="出生年月")
	interest = models.TextField(blank=True, null=True, verbose_name="兴趣爱好")

	integrity = models.IntegerField(blank=True, null=True, verbose_name="信息完整度")
	score = models.IntegerField(blank=True, null=True)

	uber_benefit = models.BooleanField(default=False)

	objects = UserManager()

	def __str__(self):
		if self.username:
			return self.username
		else:
			return str(self.id)


class EducationExpericence(models.Model):
	user = models.ForeignKey(User)
	school = models.CharField(max_length=50, verbose_name="学校名称")
	major = models.CharField(max_length=50, verbose_name="所学专业")
	degree_choices = (
		('J', 'Junior college'),
		('B', 'Bachelor'),
		('M', 'Master'),
		('P', 'PhD'),
		('R', 'Reading'),
	)
	gpa_score = models.FloatField(blank=True, null=True)
	gpa_total = models.FloatField(blank=True, null=True)
	course = models.CharField(max_length=100, blank=True, null=True, verbose_name="所修课程")
	degree = models.CharField(max_length=1, choices=degree_choices, default='B', verbose_name="所获学位")
	grade = models.CharField(max_length=20, blank=True, null=True, verbose_name="在读年级")
	start_date = models.DateField()
	end_date = models.DateField(blank=True, null=True)
	is_activated = models.BooleanField(default=True)

	def __str__(self):
		if self.user.username:
			return self.user.username
		else:
			return str(self.user.id)


class WorkExperience(models.Model):
	user = models.ForeignKey(User)
	company = models.CharField(max_length=50, blank=True, verbose_name="公司名")
	position = models.CharField(max_length=50, blank=True, verbose_name="职位")
	department = models.CharField(max_length=50, blank=True, null=True, verbose_name="部门")
	duties = models.TextField(blank=True, null=True, verbose_name="职责")
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	is_activated = models.BooleanField(default=True)

	def get_start_date(self):
		return "%i.%i.%i" % (self.start_date.year, self.start_date.month, self.start_date.day)

	def get_end_date(self):
		return "%i.%i.%i" % (self.end_date.year, self.end_date.month, self.end_date.day)

	def get_start_date_2(self):
		return "%i-%i-%i" % (self.start_date.year, self.start_date.month, self.start_date.day)

	def get_end_date_2(self):
		return "%i-%i-%i" % (self.end_date.year, self.end_date.month, self.end_date.day)

	def __str__(self):
		if self.user.username:
			return self.user.username
		else:
			return str(self.user.id)


class SocialWorkExperience(models.Model):
	user = models.ForeignKey(User)
	associations = models.CharField(max_length=50, blank=True, null=True, verbose_name="社团名")
	area = models.CharField(max_length=50, blank=True, null=True, verbose_name="地区")
	position = models.CharField(max_length=50, blank=True, verbose_name="职位")
	duties = models.TextField(blank=True, null=True, verbose_name="职责")
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	is_activated = models.BooleanField(default=True)

	def __str__(self):
		if self.user.username:
			return self.user.username
		else:
			return str(self.user.id)



class Language(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=50, blank=True, null=True, verbose_name="语言名")
	proficiency_choices = (
		('M', '母语'),
		('F', '流利'),
		('G', '一般'),
	)
	proficiency = models.CharField(max_length=50, choices=proficiency_choices, blank=True, null=True, verbose_name="熟练度")
	subject = models.CharField(max_length=50, blank=True, null=True, verbose_name="科目")
	score = models.CharField(max_length=50, blank=True, null=True, verbose_name="成绩")
	is_activated = models.BooleanField(default=True)

	def __str__(self):
		if self.user.username:
			return self.user.username
		else:
			return str(self.user.id)


class Certificate(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=50, blank=True, null=True, verbose_name="证书名")
	is_activated = models.BooleanField(default=True)

	def __str__(self):
		if self.user.username:
			return self.user.username
		else:
			return str(self.user.id)


class Software(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=50, blank=True, null=True, verbose_name="软件名")
	proficiency_choices = (
		('P', '精通'),
		('S', '熟练'),
		('G', '一般'),
	)
	proficiency = models.CharField(max_length=50, choices=proficiency_choices, blank=True, null=True, verbose_name="熟练度")
	is_activated = models.BooleanField(default=True)

	def __str__(self):
		if self.user.username:
			return self.user.username
		else:
			return str(self.user.id)



class Resume(models.Model):
	user = models.ForeignKey(User)
	resume = models.FileField(upload_to=resume_path)
	filename = models.CharField(blank=True, max_length=200)
	date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	is_defaulted = models.BooleanField(default=False)
	is_activated = models.BooleanField(default=True)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.user.__str__()

	def get_date(self):
		return "%i-%i-%i" % (self.date.year, self.date.month, self.date.day)


class CompanyManager(models.Manager):
	def create_company(self, email, pwd):
		time = timezone.now()
		company = self.create(email=email, copwd=pwd, register_date=time, last_login_date=time)
		return company


class Company(models.Model):
	unique_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
	coname = models.CharField(blank=True, max_length=50)
	copwd = models.CharField(max_length=80)
	email = models.EmailField(max_length=50)
	address = models.CharField(blank=True, max_length=100)
	latitude = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=7)
	longitude = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=7)
	scale = models.CharField(blank=True, max_length=20)
	domain = models.CharField(blank=True, max_length=100)
	description = models.TextField(blank=True, max_length=5000)
	website = models.URLField(blank=True)
	benefit = models.CharField(blank=True, max_length=100, verbose_name='公司福利')
	logo = models.ImageField(blank=True, upload_to='logo')
	register_date = models.DateTimeField(blank=True, null=True)
	last_login_date = models.DateTimeField(blank=True, null=True)
	is_vip = models.BooleanField(default=False)
	is_activated = models.BooleanField(default=False)
	company_score = models.IntegerField(default=0)
	company_oldscore = models.IntegerField(default=0)
	ip = models.CharField(blank=True, max_length=30, null=True)
	paper_plane_num = models.IntegerField(default=0, verbose_name='收到的纸飞机')
	login_num = models.IntegerField(default=0)  #统计每个账号的登陆总数

	uber_benefit = models.BooleanField(default=False)

	objects = CompanyManager()

	def __str__(self):
		if self.coname:
			return self.coname
		else:
			return str(self.id)


class Job(models.Model):
	company = models.ForeignKey(Company)
	category = models.CharField(blank=True, max_length=50, verbose_name='标签')
	position = models.CharField(max_length=100, verbose_name='职位')
	department = models.CharField(blank=True, max_length=50, verbose_name='部门')
	worktype_choices = (
		('FT', 'Full-time'),
		('IN', 'Intern')
	)
	worktype = models.CharField(max_length=2, choices=worktype_choices, default='FT')
	acceptnum = models.IntegerField(blank=True,null=True)
	lowsalary = models.CharField(blank=True, null=True, max_length=20)
	highsalary = models.CharField(blank=True, null=True, max_length=20)
	city = models.CharField(blank=True, max_length=50)
	experience = models.CharField(blank=True, max_length=20)
	degree = models.CharField(blank=True, max_length=20)
	address = models.CharField(blank=True, max_length=100)
	latitude = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=7)
	longitude = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=7)
	duty = models.TextField(blank=True, max_length=4000)
	demand = models.TextField(blank=True, max_length=4000)
	datetime = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	is_activated = models.BooleanField(default=True)
	is_hot = models.BooleanField(default=False)
	refresh = models.DateField(blank=True, null=True)
	ip = models.CharField(blank=True, max_length=30, null=True)
	top = models.BooleanField(default=False)

	contacts = models.CharField(blank=True, null=True, max_length=50, verbose_name='联系人')
	phone = models.CharField(blank=True, null=True, max_length=20)
	interaddress = models.CharField(blank=True, null=True, max_length=100, verbose_name='面试地点')
	memo = models.CharField(blank=True, null=True, max_length=100, verbose_name='备注')


	def __str__(self):
		return "%i %s" % (self.id, self.position)

	def get_resume_num(self):
		return len(Application.objects.filter(job=self, isrejected=False))

	def get_video_num(self):
		n = 0
		apps = Application.objects.filter(job=self)
		for app in apps:
			videos = Video.objects.filter(application=app)
			if len(videos) > 0:
				n += 1
		return n

	def get_resume_url(self):
		return '/applications/?query=resume&jobid=%i' % self.id

	def get_video_url(self):
		return '/applications/?query=video&jobid=%i' % self.id

	def get_deactivate_url(self):
		return '/deactivatejob/%i/' % self.id

	def get_activate_url(self):
		return '/activatejob/%i/' % self.id



class Topic(models.Model):
	job = models.ForeignKey(Job)
	content = models.CharField(max_length=100)
	duration_choices = (
		(30, '30 seconds'),
		(60, '60 seconds'),
		(90, '90 seconds'),
		(120, '120 seconds'),
	)
	duration = models.IntegerField(choices=duration_choices, default=60)

	def __str__(self):
		return self.content


class Application(models.Model):
	unique_id = models.CharField(max_length=100, default=uuid.uuid4)
	user = models.ForeignKey(User)
	job = models.ForeignKey(Job)
	resume = models.ForeignKey(Resume, null=True)
	status_choices = (
		('SU', 'Submitted'),
		('AC', 'Accepted'),
		('RJ', 'Rejected'),
		('RP', 'Reposted'),
		('RE', 'Read'),
		('TO', 'Timeout/OffLine'),
		('IN', 'Interview'),
	)
	status = models.CharField(max_length=2, choices=status_choices, default='SU')
	isreposted = models.BooleanField(default=False)
	isread = models.BooleanField(default=False)
	isrejected = models.BooleanField(default=False)
	isupdated = models.BooleanField(default=False)
	istimeout = models.BooleanField(default=False)
	isinterview = models.BooleanField(default=False, verbose_name='面试')
	time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	reposttime = models.DateTimeField(blank=True, null=True)
	readtime = models.DateTimeField(blank=True, null=True)
	rejecttime = models.DateTimeField(blank=True, null=True)
	accepttime = models.DateTimeField(blank=True, null=True)
	rejected = models.IntegerField(blank=True, null=True)
	timeouttime = models.DateTimeField(blank=True, null=True)
	interviewtime = models.DateTimeField(blank=True, null=True, verbose_name='面试时间')
	review = models.TextField(blank=True, null=True)
	is_new = models.NullBooleanField(blank=True, null=True, default=True)
	downtime = models.DateTimeField(blank=True, null=True)
	olresume = models.BooleanField(default=False)
	feedback = models.TextField(blank=True, null=True)
	hrfeedback = models.TextField(blank=True, null=True)


	def __str__(self):
		return "User: %s, Job: %s" % (self.user.__str__(), self.job.__str__())

	# def get_resume_url(self):
	#	return "/viewResume/%i/" % self.id

	#def get_video_url(self):
	#	return "/viewVideo/%i/" % self.id

	def update_read_url(self):
		return "/updateStatus/%i/0/" % self.id

	def update_rejected_url(self):
		return "/updateStatus/%i/1/" % self.id

	def update_accepted_url(self):
		return "/updateStatus/%i/2/" % self.id

	def update_reposted_url(self):
		return "/updateStatus/%i/3/" % self.id

	def update_reverse_url(self):
		return "/updateStatus/%i/4/" % self.id

	def update_updated_url(self):
		return "/updateStatus/%i/5/" % self.id

	def get_review_url(self):
		return "http://www.careerdream.org/repostpreview/?appid=%s" % self.unique_id

	def get_time(self):
		hour = str(self.time.hour)
		if self.time.hour < 10:
			hour = '0' + hour
		minute = str(self.time.minute)
		if self.time.minute < 10:
			minute = '0' + minute
		return '%i-%i-%i %s:%s' % (self.time.year, self.time.month, self.time.day, hour, minute)

	def get_reposttime(self):
		hour = str(self.reposttime.hour)
		if self.reposttime.hour < 10:
			hour = '0' + hour
		minute = str(self.reposttime.minute)
		if self.reposttime.minute < 10:
			minute = '0' + minute
		return '%i-%i-%i %s:%s' % (self.reposttime.year, self.reposttime.month, self.reposttime.day, hour, minute)

	def get_readtime(self):
		hour = str(self.readtime.hour)
		if self.readtime.hour < 10:
			hour = '0' + hour
		minute = str(self.readtime.minute)
		if self.readtime.minute < 10:
			minute = '0' + minute
		return '%i-%i-%i %s:%s' % (self.readtime.year, self.readtime.month, self.readtime.day, hour, minute)

	def get_rejecttime(self):
		hour = str(self.rejecttime.hour)
		if self.rejecttime.hour < 10:
			hour = '0' + hour
		minute = str(self.rejecttime.minute)
		if self.rejecttime.minute < 10:
			minute = '0' + minute
		return '%i-%i-%i %s:%s' % (self.rejecttime.year, self.rejecttime.month, self.rejecttime.day, hour, minute)

	def get_accepttime(self):
		hour = str(self.accepttime.hour)
		if self.accepttime.hour < 10:
			hour = '0' + hour
		minute = str(self.accepttime.minute)
		if self.accepttime.minute < 10:
			minute = '0' + minute
		return '%i-%i-%i %s:%s' % (self.accepttime.year, self.accepttime.month, self.accepttime.day, hour, minute)

	def get_timeouttime(self):
		hour = str(self.timeouttime.hour)
		if self.timeouttime.hour < 10:
			hour = '0' + hour
		minute = str(self.timeouttime.minute)
		if self.timeouttime.minute < 10:
			minute = '0' + minute
		return '%i-%i-%i %s:%s' % (self.timeouttime.year, self.timeouttime.month, self.timeouttime.day, hour, minute)


class Video(models.Model):
	application = models.ForeignKey(Application)
	topic = models.ForeignKey(Topic)
	path = models.FilePathField(path=video_path)


class Log(models.Model):
	userid = models.CharField(max_length=20, blank=True)
	type_choices = (
		('u', 'user'),
		('w', 'wechat_user'),
		('c', 'company')
	)
	usertype = models.CharField(max_length=2, choices=type_choices, blank=True)
	url = models.CharField(blank=True, max_length=200)
	ip = models.CharField(blank=True, max_length=30)
	time = models.DateTimeField(blank=True, auto_now_add=True)
	timestamps = models.FloatField()



class Article(models.Model):
	title = models.CharField(blank=True, max_length=500)  # 标题
	author = models.CharField(blank=True, max_length=100)  # 作者
	articles = models.TextField(blank=True, max_length=5000)  # 内容
	smallimg = models.ImageField('缩略图', blank=True, upload_to='titleimg')
	titleimg = models.ImageField(blank=True, upload_to='titleimg')  # 图片
	category = models.CharField(blank=True, max_length=100)  # 分类
	datetime = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	click = models.IntegerField(default=0)

class Image(models.Model):
	img = models.ImageField(blank=True, upload_to='./img')


class logintime(models.Model):
	user = models.ForeignKey(User, null=True)
	company = models.ForeignKey(Company, null=True)
	time = models.DateTimeField(blank=True, auto_now=True)




def get_work_exp_years(user):
	import datetime as dt
	now = dt.date.today()
	work_exps = WorkExperience.objects.filter(user=user, is_activated=True)
	day = 0
	if work_exps.count() == 0:
		return day
	for work_exp in work_exps:
		if not work_exp.end_date:
			work_exp.end_date = dt.date(now.year, now.month, now.day)
		day += (work_exp.end_date - work_exp.start_date).days
	years = round(day/365)
	return years

class Comment(models.Model):
	ucomment = models.ForeignKey(User, null=True)
	ccomment = models.ForeignKey(Company, null=True)
	ment_companyid = models.CharField(max_length=100,null=True)
	comments = models.TextField(blank=True,max_length=200)
	comm_time = models.DateTimeField(blank=True,null=True,auto_now_add=True)
	type_choices = (
		('s','support'),
		('o','opposition'),
	)
	position = models.CharField(max_length=2,choices=type_choices,default='s')
	quote_who = models.CharField(max_length=100, null=True)
	anonymous = models.BooleanField(default=False)
	delete = models.BooleanField(default=False)
