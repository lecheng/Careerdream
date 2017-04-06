# coding: utf-8
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "careerdream.settings")

import django

django.setup()

from main.models import Application, Company, Job
import simplejson

def genCycleJson():
	appsSub = Application.objects.filter(status='SU').order_by('-time')[:240]
	appsRead = Application.objects.filter(status='RE').order_by('-readtime')[:100]
	appsForward = Application.objects.filter(status='RP').order_by('-reposttime')[:100]
	allList = list()
	companyTotal = Company.objects.all().count()
	postTotal = Job.objects.all().count()
	for app in appsSub:
		d = dict()
		d['name'] = app.user.username
		d['status'] = app.status
		d['company'] = app.job.company.coname
		d['time'] = app.time
		allList.append(d)
	for app in appsRead:
		d = dict()
		d['name'] = app.user.username
		d['status'] = app.status
		d['company'] = app.job.company.coname
		d['time'] = app.readtime
		allList.append(d)
	for app in appsForward:
		d = dict()
		d['name'] = app.user.username
		d['status'] = app.status
		d['company'] = app.job.company.coname
		d['time'] = app.reposttime
		allList.append(d)
	k = lambda k: k['time']
	allList = sorted(allList, key=k, reverse=True)
	json = {
		'allList': allList,
		'companyTotal': companyTotal,
		'postTotal': postTotal
	}
	return json

if __name__ == '__main__':
	json = genCycleJson()
	for i in json['allList']:
		print(i['time'],i['status'])
	with open('FeaturedPages.json', 'w') as f:
		for item in json['allList']:
			item.pop('time')
		simplejson.dump(json, f)
