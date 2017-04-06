from main.models import Application


# 用在简历管理, 获取apps
def get_apps(jobid, category, option, company):
	apps = Application.objects
	if jobid:
		apps = apps.filter(job__id=jobid)
	else:
		apps = apps.filter(job__company=company)

	if category == 1:
		apps = apps.exclude(status='RJ').exclude(status='TO').exclude(status='IN')
	elif category == 2:
		apps = apps.filter(status='SU')
	elif category == 3:
		apps = apps.filter(status='RJ')
	elif category == 4:
		apps = apps.filter(status='IN')
	else:
		return False

	if option == 1:
		apps = apps.order_by('-time')
	elif option == 2:
		apps = apps.order_by('-resume__score')
	elif option == 3:
		apps = apps.filter(resume__score__gte=85).order_by('-time')
	else:
		return False
	return apps
