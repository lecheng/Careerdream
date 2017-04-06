# coding: utf-8
from email import encoders, mime
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import os
import smtplib
import datetime


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'admin@careerdream.org'
password = 'Dream_123@'
smtp_server = 'email.careerdream.org'

def sendmail(to_addr, title, content):
	msg = MIMEText(content, 'plain', 'utf-8')
	msg['From'] = _format_addr(from_addr)
	msg['To'] = ','.join(to_addr)
	msg['Subject'] = Header(title, 'utf-8').encode()

	try:
		server = smtplib.SMTP(smtp_server, 25)
		server.set_debuglevel(1)
		server.login(from_addr, password)
		server.sendmail(from_addr, to_addr, msg.as_string())
		server.quit()
		re = True
	except Exception as e:
		re = False
	return re

def sendMailToUser(app, status):
	msg = mime.multipart.MIMEMultipart()
	msg['from'] = 'contact@careerdream.cn'
	if status == 'read':
		msg['subject'] = app.job.company.coname + '简历投递状态更新通知——被查看'
	elif status == 'forward':
		msg['subject'] = app.job.company.coname + '简历投递状态更新通知——被转发'
	elif status == 'reject':
		msg['subject'] = app.job.company.coname + '简历投递状态更新通知——不匹配'
	elif status == 'interview':
		msg['subject'] = app.job.company.coname + '简历投递状态更新通知——面试邀约'
	msg['to'] = app.user.email
	# msg['cc'] = 'hr@careerdream.org'
	username = app.user.username
	if username == '':
		username = '职业梦用户'
	if status == 'read':
		content = '''<html><body>
					亲爱的''' + username +'''，您好！
				<br><br>
					您在职业梦<a href='http://www.careerdream.org'>www.careerdream.org</a>网站上投递''' + app.job.company.coname + app.job.department + app.job.position + '''的简历已被<strong style="font-size: 125%">HR查看</strong>，企业会尽快反馈考评结果，请静候佳音。
		'''
	elif status == 'forward':
		content = '''<html><body>
					亲爱的''' + username +'''，恭喜您！
				<br><br>
					您在职业梦<a href='http://www.careerdream.org'>www.careerdream.org</a>网站上投递''' + app.job.company.coname + app.job.department + app.job.position + '''的简历通过了综合考评，<strong style="font-size: 125%">HR已将您简历转发给相关用人部门</strong>，如合适企业将与您直接进行沟通联系。
		'''
	elif status == 'reject':
		content = '''<html><body>
					亲爱的''' + username +'''，您好！
				<br><br>
					您在职业梦<a href='http://www.careerdream.org'>www.careerdream.org</a>网站上投递''' + app.job.company.coname + app.job.department + app.job.position + '''的简历已被HR查看，但是经过招聘方多方面评估，很遗憾您与该职位应聘条件<strong style="font-size: 125%">被标注为不匹配</strong>，无法进入面试环节。
				<br><br>
					职业梦希望您再接再厉，早日收到面试邀请。
		'''
	elif status == 'interview':
		content = '''<html><body>
					亲爱的''' + username +'''，您好！
				<br><br>
					非常荣幸的通知您。经过''' + app.job.company.coname + '''的筛选，决定向您发出面试邀请。详情如下：
				<br><br>
					面试职位: ''' + app.job.position + '''
					<br>
					面试时间: ''' + app.interviewtime + '''
					<br>
					面试地点: ''' + app.job.interaddress + '''
					<br>
					联系人  : ''' + app.job.contacts + '''
					<br>
					联系电话: ''' + app.job.phone + '''
					<br>
					'''
		if app.job.memo:
			content += '''面试备忘: ''' + app.job.memo + '''
					'''

	content += '''
				<br><br>
					查看更多动态变动请<a href='http://www.careerdream.org/login_in.html' style="color: blue; cursor: pointer">点击这里</a>
				<br><br>
					感谢您一直以来对职业梦的信任，职业梦因你而更加精彩；如有任何宝贵建议，请随时与我们反馈。
				<br><br>
					------------------------------------------------------------------------------------
				<br><br>
					职业梦小编Alice 金雪
				<br>
					24小时客服电话：+86-400-022-5780
				<br>
					微信号：careerdream/alicezym0313
				<br>
					海淀区海淀大街11号E世界财富中心C座B2层
				<br>
					</body></html>
	'''
	txt = mime.text.MIMEText(content, 'html')
	msg.attach(txt)
	smtp = smtplib.SMTP()
	smtp.connect(smtp_server, '25')
	smtp.login(from_addr, password)
	smtp.sendmail(from_addr, msg['to'], msg.as_string())
	smtp.quit()
	# Logs
	date = datetime.datetime.now()
	filename = '/root/logs/email_to_user/'+str(date.date())+'.txt'
	if os.path.exists(filename):
		f = open(filename, 'r')
		content = f.read()
		line = content.split('\n')[-2]
		n = int(line.split(' ')[0])+1
		f.close()
	else:
		n = 1
	f = open(filename, 'a+')
	f.write('%d %s %s\n' % (n, str(date), msg['to']))
	f.close()
