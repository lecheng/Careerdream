from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from main.models import *
from data.models import *
from django.db.models import Q, Count

import json
import simplejson
import datetime as dt

# Create your views here.
@csrf_exempt
def dataSignin(request):
	return render(request, 'data_login.html')

@csrf_exempt
def dataIndex(request):
	return render(request, 'index.html')

@csrf_exempt
def dataNewCompany(request):
	if request.session.get('data_is_login'):
		companyids = []
		result = []
		logs = Log.objects.filter(usertype='c').exclude(ip='118.26.133.2').values('userid').annotate(Count('userid'))
		for i in logs:
			if i:
				item = {}
				companyid = i['userid']
				if companyid:
					companys = Company.objects.filter(id=companyid)
					if companys:
						company = companys[0]
						item['id'] = company.id
						item['email'] = company.email
						item['coname'] = company.coname
						item['create_time'] = company.register_date
						item['last_login_date'] = company.last_login_date
						item['jobnum'] = company.job_set.count()
						result += [item]
		return render(request, 'data_newb.html', {'Result': result})
	else:
		return HttpResponseRedirect('/signin')


@csrf_exempt
def dataLogin(request):
	if request.method == 'POST':
		pwd = request.POST.get('password')
		if pwd == 'youcanyouup':
			request.session['data_is_login'] = 1
			return render(request, 'data_selc.html')
		else:
			return HttpResponse('password error!')
	else:
		return HttpResponseRedirect('/signin')


@csrf_exempt
def datajob(request):
	if request.session.get('data_is_login'):
		result = []
		jobs = Job.objects.all()
		jobs = Application.objects.values('job_id').annotate(Count('job_id')).order_by('-job_id__count')[0:99]
		for i in jobs:
			item = {}
			job = Job.objects.get(pk=i['job_id'])
			item['coname'] = job.company.coname
			item['companyemail'] = job.company.email
			item['department'] = job.department
			item['position'] = job.position
			item['datetime'] = job.datetime
			item['sumapp'] = job.application_set.count()
			item['unreadapp'] = job.application_set.filter(status='SU').count()
			item['readapp'] = job.application_set.filter(isread=True).count()
			item['repostapp'] = job.application_set.filter(isreposted=True).count()
			item['rejectapp'] = job.application_set.filter(isrejected=True).count()
			result += [item]
		result = sorted(result, key=lambda item: item['sumapp'], reverse=True)
		return render(request, 'data_hero.html', {'Result': result})
	else:
		return HttpResponseRedirect('/signin')


@csrf_exempt
def updateData(request):
	if request.method == 'POST':
		code = request.POST.get('code', '')
		if code == 'f0f9e1969e45e2768d655f9c54ad21a6dd66115c':
			time_delta = dt.timedelta(days=1)
			end_date = dt.datetime.now()
			if DailyRecord.objects.all().count() == 0:
				start_date = dt.datetime(2015, 3, 18)
			else:
				start_date = DailyRecord.objects.all().order_by('datetime').reverse()
				start_date = start_date[0].datetime + time_delta
			current_date = start_date
			prev_date = start_date - time_delta
			c_prev_login_num = User.objects.filter(last_login_date__gte=prev_date,
												   last_login_date__lt=current_date).count()
			# b_prev_login_num = Company.objects.filter(last_login_date__gte=prev_date, last_login_date__lt=current_date).count()
			end_date = end_date - time_delta
			while current_date < end_date:
				next_date = current_date + time_delta
				c_login_num = User.objects.filter(last_login_date__gte=current_date,
												  last_login_date__lt=next_date).count()
				c_new_reg_num = User.objects.filter(register_date__gte=current_date,
													register_date__lt=next_date).count()
				# b_login_num = Company.objects.filter(last_login_date__gte=current_date, last_login_date__lt=next_date).count()
				# b_new_reg_num = Company.objects.filter(register_date__gte=current_date, register_date__lt=next_date).count()	
				if c_prev_login_num == 0:
					c_prev_login_num = 1
				# if b_prev_login_num == 0:
				# 	b_prev_login_num = 1
				rc = (c_login_num - c_new_reg_num) / c_prev_login_num * 100
				# rb = (b_login_num-b_new_reg_num) / b_prev_login_num * 100
				c_prev_login_num = c_login_num
				# b_prev_login_num = b_login_num
				newRecord = DailyRecord.objects.create_record(current_date, rc)
				newRecord.save()
				current_date = current_date + time_delta
			return HttpResponse('update data')
		else:
			return HttpResponse('wrong code')
	else:
		return HttpResponse('method error')

@csrf_exempt
def creport(request):
	if request.session.get('data_is_login'):
		alldata = User_Active.objects.order_by('-datetime')
		return render(request, "data_report_c.html", {'alldata': alldata})
	else:
		return HttpResponseRedirect('/signin')


@csrf_exempt
def dataFeedback(request):
	# B端反馈情况
	if request.session.get('data_is_login'):
		data = DailyPosition.objects.order_by('-datetime')
		jsonlist = []
		for i in data:
			jsons = {
				'datetime': str(i.datetime),
				'c_read': i.c_read,
				'c_forward': i.c_forward,
				'c_mark': i.c_mark,
				'c_expire': i.c_expire,
				'c_works': i.c_works,
				'average_application': i.average_application,
				'daily_refresh': i.daily_refresh,
				'b_down': str(i.b_down) if i.b_down else '0',
				'position_due': str(i.position_due) if i.position_due else '0',
				'date_aver': str(i.date_aver) if i.date_aver else '0',
				'match_total': str(i.match_total) if i.match_total else '0',
				'position':str(i.position) if i.position else '0',
			}
			jsonlist += [jsons]
		result = {
			'json': jsonlist
		}
		return HttpResponse(json.dumps(result))
	else:
		return HttpResponse('/signin')

@csrf_exempt
def dataReg(request):
	# 注册量
	if request.session.get('data_is_login'):
		data = DataReg.objects.filter().order_by('-datetime')
		jsonlist = []
		for i in data:
			jsons = {
				'datetime': str(i.datetime),
				'c_user_reg': i.c_user_reg,
				'b_total': i.b_total,
				'b_active_reg': i.b_active_reg,
				'b_passive_reg': i.b_passive_reg,
				'c_reg_total': i.c_reg_total,
				'b_reg_total': i.b_reg_total,
				'b_active_total': i.b_active_total,
				'b_passive_total': i.b_passive_total,
				'b_active_singin':str(i.b_active_singin) if i.b_active_singin else '0',
				'b_account':str(i.b_account) if i.b_account else '0',
			}
			jsonlist += [jsons]
		result = {
			'json': jsonlist
		}
		return HttpResponse(json.dumps(result))
	else:
		return HttpResponse('/signin')

@csrf_exempt
def dataBactive(request):
	# B端活跃情况
	if request.session.get('data_is_login'):
		data = DataBactive.objects.filter().order_by('-datetime')
		jsonlist = []
		for i in data:
			jsons = {
				'datetime': str(i.datetime),
				'user_active': i.user_active,
				'user_loss': i.user_loss,
				'loss_rate': str(i.loss_rate),
				'return_rate': i.return_rate,
				'not_active': i.not_active,
				'not_active_rate': str(i.not_active_rate),
			}
			jsonlist += [jsons]
		result = {
			'json': jsonlist
		}
		return HttpResponse(json.dumps(result))
	else:
		return HttpResponse('/signin')

@csrf_exempt
def dataCactive(request):
	# C端活跃情况
	if request.session.get('data_is_login'):
		data = DataCactive.objects.filter().order_by('-datetime')
		jsonlist = []
		for i in data:
			jsons = {
				'datetime': str(i.datetime),
				'user_active': i.user_active,
				'user_loss': i.user_loss,
				'loss_rate': str(i.loss_rate),
				'return_rate': i.return_rate,
				'not_active': i.not_active,
				'not_active_rate': str(i.not_active_rate),
			}
			jsonlist += [jsons]
		result = {
			'json': jsonlist
		}
		return HttpResponse(json.dumps(result))
	else:
		return HttpResponse('/signin')

@csrf_exempt
def dataResume(request):
	# 简历投递情况
	if request.session.get('data_is_login'):
		data = DataResume.objects.filter().order_by('-datetime')
		jsonlist = []
		for i in data:
			jsons = {
				'datetime':str(i.datetime),
				'pos_aver':str(i.pos_aver),
				'resume_total':i.resume_total,
				'new_delivery':i.new_delivery,
				'c_delivery':str(i.c_delivery),
				}
			jsonlist += [jsons]
		result = {
			'json': jsonlist
		}
		return HttpResponse(json.dumps(result))
	else:
		return HttpResponse('/signin')

@csrf_exempt
def dataPosition(request):
	# 职位信息
	if request.session.get('data_is_login'):
		data = DataPosition.objects.all().order_by('-datetime')
		jsonlist = []
		for i in data:
			jsons = {
				'datetime':str(i.datetime),
				'position_total':i.position_total,
				'add_position':i.add_position,
				'aver_position':str(i.aver_position),
				'loss_add':i.loss_add,
				'loss_aver':str(i.loss_aver),
				}
			jsonlist += [jsons]
		result = {
			'json': jsonlist
		}
		return HttpResponse(json.dumps(result))


	else:
		return HttpResponse('/signin')

@csrf_exempt
def dataComment(request):
	# savelog(request)
	if request.session.get('data_is_login'):
		# today = dt.date.today()
		# yesterday = today - dt.timedelta(1)
		result = CommentData.objects.exclude(date_comment='0').order_by('-datetime')
		return render(request, 'data_comment.html', {'Result': result})
	else:
		return HttpResponse('/signin')
