# coding: utf-8
import os
import sys
import re
import simplejson

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "careerdream.settings")

import django

django.setup()

from main.models import Company

from pypinyin import lazy_pinyin

filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'hans2pinyin.json')

def get_all_company():
	return Company.objects.all()

def gen_pinyin_dict(companys):
	result = dict()
	for company in companys:
		coname = company.coname
		if coname:
			pinyin = lazy_pinyin(coname)
			if coname not in result.keys():
				result[coname] = ''.join(pinyin)
	return result

def gen_json_file(filepath, json):
	with open(filepath, 'a+') as f:
		simplejson.dump(json, f)
	return True

def get_json_data(filepath=filepath):
	with open(filepath) as f:
		result = simplejson.load(f)
	return result

def get_search_list(search, json):
	data = list()
	for k, v in json.items():
		if search.isalpha():
			match = re.compile(search)
			result = match.findall(v)
			if len(result) > 0:
				data.append(k)
	return data

if __name__ == '__main__':
	companys = get_all_company()
	json = gen_pinyin_dict(companys)
	gen_json_file(filepath, json)
