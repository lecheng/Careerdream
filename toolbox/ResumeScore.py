# coding: utf-8

import re
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "careerdream.settings")

import django

django.setup()

from main.models import User, EducationExpericence, WorkExperience, SocialWorkExperience, Certificate, Software, \
	Language

from toolbox.MatchLibrary import SchoolKeyword, MajorKeyword, CompanyKeyword, LeadershipKeyword, WorkContentKeyword, \
	LanguageKeywords, CertificateKeyword, SoftwareKeyword


# 简历完整度
def resumeIntegrity(userid):
	user = User.objects.get(id=userid)
	integrity = 0

	# 基本信息
	if user.username:
		integrity += 5
	if user.avatar:
		integrity += 3
	if user.phone:
		integrity += 5
	if user.gender:
		integrity += 2
	if user.birth:
		integrity += 2
	if user.city:
		integrity += 2

	# 教育经历
	eduexp = EducationExpericence.objects.filter(user=user, is_activated=True)
	GPA = False
	if eduexp:
		integrity += 19
		for item in eduexp:
			if item.gpa_score and item.gpa_total:
				GPA = True
			if GPA:
				break
	if GPA:
		integrity += 2

	# 工作经历
	workexp = WorkExperience.objects.filter(user=user, is_activated=True)
	department = False
	if workexp:
		integrity += 17
		for item in workexp:
			if item.department:
				department = True
			if department:
				break
	if department:
		integrity += 3

	# 社工经历
	socialworkexp = SocialWorkExperience.objects.filter(user=user, is_activated=True)
	area = False
	if socialworkexp:
		integrity += 13
		for item in socialworkexp:
			if item.area:
				area = True
			if area:
				break
	if area:
		integrity += 3

	# 语言
	language = Language.objects.filter(user=user, is_activated=True)
	subject = False
	score = False
	if language:
		integrity += 5
		for item in language:
			if item.subject:
				subject = True
			if item.score:
				score = True
			if subject and score:
				break
	if subject:
		integrity += 3
	if score:
		integrity += 3

	# 证书
	certificate = Certificate.objects.filter(user=user, is_activated=True)
	if certificate:
		integrity += 3

	# 软件
	software = Software.objects.filter(user=user, is_activated=True)
	if software:
		integrity += 5

	# 兴趣爱好
	if user.interest:
		integrity += 5

	user.integrity = integrity
	user.save()
	return integrity


# 简历评分
def resumeScore(userid):
	user = User.objects.get(id=userid)
	score = 0

	# 基础分
	schoolScore = 0
	majorScore = 0
	gpaScore = 0
	companyScore = 0
	positionScore = 0
	languageScore = 0
	certificateScore = 0

	counter = 0
	WorkContentList = list()
	SoftwareList = list()

	# 教育经历
	eduexp = EducationExpericence.objects.filter(user=user, is_activated=True)
	for item in eduexp:

		# min score
		if schoolScore == 0:
			schoolScore = 10
		if majorScore == 0:
			majorScore = 3

		# 学校加分
		school = item.school
		for k, v in SchoolKeyword.items():
			for word in v:
				match = re.compile(r'%s' % word, re.UNICODE)
				result = match.findall(school)
				if len(result) > 0:
					if k >= schoolScore:
						schoolScore = k

		# 专业加分
		major = item.major
		for k, v in MajorKeyword.items():
			for word in v:
				match = re.compile(r'%s' % word, re.UNICODE)
				result = match.findall(major)
				if len(result) > 0:
					if k >= majorScore:
						majorScore = k

		# GPA加分
		selfgpa = item.gpa_score
		maxgpa = item.gpa_total
		if selfgpa and maxgpa:
			gpa = selfgpa / maxgpa
			if gpa <= 0.05:
				k = 5
			elif gpa <= 0.1:
				k = 4
			elif gpa <= 0.2:
				k = 3
			elif gpa <= 0.4:
				k = 2
			if k >= gpaScore:
				gpaScore = k

	# 工作经历
	workexp = WorkExperience.objects.filter(user=user, is_activated=True)
	for item in workexp:

		# min score
		if companyScore == 0:
			companyScore = 15

		# 公司加分
		company = item.company
		lock = 1
		for k, v in CompanyKeyword.items():
			for word in v:
				match = re.compile(r'%s' % word, re.UNICODE)
				result = match.findall(company)
				if len(result) > 0:
					if lock:
						counter += 1  # 匹配到的次数
						lock = 0
					if k >= companyScore:
						companyScore = k

		# 工作内容加分
		duties = item.duties
		for word in WorkContentKeyword:
			if len(WorkContentList) == 10:
				break
			match = re.compile(r'%s' % word, re.UNICODE)
			result = match.findall(str(duties))
			if len(result) > 0 and result[0] not in WorkContentList:
				WorkContentList.append(result[0])
		# 职位
		position = item.position
		for k, v in LeadershipKeyword.items():
			for word in v:
				match = re.compile(r'%s' % word, re.UNICODE)
				result = match.findall(position)
				if len(result) > 0:
					if k >= positionScore:
						positionScore = k

	# 社会工作经历
	socialworkexp = SocialWorkExperience.objects.filter(user=user, is_activated=True)

	for item in socialworkexp:

		# min score
		if positionScore == 0:
			positionScore = 6

		# 领导能力加分
		position = item.position
		for k, v in LeadershipKeyword.items():
			for word in v:
				match = re.compile(r'%s' % word, re.UNICODE)
				result = match.findall(position)
				if len(result) > 0:
					if k >= positionScore:
						positionScore = k

	# 语言
	language = Language.objects.filter(user=user, is_activated=True)
	for item in language:

		if languageScore == 5:
			break

		# 语言加分
		languagename = item.name
		if languagename == '英语':
			subject = item.subject
			sscore = item.score
			if subject and sscore:
				if str(subject).lower() in ['gmat', 'gre']:
					languageScore = 5
					break
				elif subject == '六级':
					if 600 <= int(sscore) <= 710:
						languageScore = 5
						break
					elif 500 <= int(sscore) <= 599:
						languageScore = 4
				elif subject in ['IELTS', 'ielts', '雅思']:
					if 7.5 <= float(sscore) <= 9.0:
						languageScore = 5
						break
					elif 6.5 <= float(sscore) <= 7.5:
						languageScore = 4
				elif subject in ['托福', 'toefl', 'TOEFL']:
					if 110 <= int(sscore) <= 120:
						languageScore = 5
						break
					elif 100 <= int(sscore) <= 109:
						languageScore = 4
		elif languagename in LanguageKeywords:
			languageScore = 5
			break

	# 证书
	certificate = Certificate.objects.filter(user=user, is_activated=True)
	for item in certificate:
		certificatename = item.name
		for k, v in CertificateKeyword.items():
			for word in v:
				match = re.compile(r'%s' % word, re.UNICODE)
				result = match.findall(certificatename)
				if len(result) > 0:
					if k >= certificateScore:
						certificateScore = k
	# 软件
	software = Software.objects.filter(user=user, proficiency='P', is_activated=True)
	for item in software:
		softwarename = item.name
		for word in SoftwareKeyword:
			if len(WorkContentList) == 5:
				break
			match = re.compile(r'%s' % word, re.I | re.UNICODE)
			result = match.findall(softwarename)
			if len(result) > 0 and result[0] not in WorkContentList:
				SoftwareList.append(result[0])
	# 补分
	while counter > 0:
		if companyScore + 2 <= 35:
			companyScore += 2
		elif companyScore + 1 <= 35:
			companyScore += 1
		elif schoolScore + 2 <= 20:
			schoolScore += 2
		elif schoolScore + 1 <= 20:
			schoolScore += 1
		else:
			break
		counter -= 1

	WorkContentScore = len(WorkContentList)
	softwareScore = len(SoftwareList)
	score += \
		schoolScore + majorScore + gpaScore + companyScore + WorkContentScore + positionScore + languageScore + \
		certificateScore + softwareScore
	user.score = score
	user.save()
	return score


if __name__ == '__main__':
	s = resumeScore('1')
	i = resumeIntegrity('1')
	print(s,i)
