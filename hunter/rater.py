# -*- coding: utf-8 -*-

from __future__ import division
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from hunter.constances import *
import io, sys, os, re

__autor__ = 'Raymond'


def convert_pdf_to_txt(path, password=""):
	fp = open(path, 'rb')
	parser = PDFParser(fp)
	doc = PDFDocument()
	parser.set_document(doc)
	doc.set_parser(parser)
	doc.initialize(password)
	if not doc.is_extractable:
		raise PDFTextExtractionNotAllowed
	rsrcmgr = PDFResourceManager()
	retstr = io.StringIO()
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	pages = doc.get_pages()
	for page in pages:
		interpreter.process_page(page)
	fp.close()
	device.close()
	str = retstr.getvalue()
	retstr.close()
	return str


def parse_keywords(text, keywords, limit, min, max):
	count = 0
	score = min
	for grade, tags in keywords.items():
		for tag in tags:
			if tag in text:
				print('  hit: ' + tag)
				count += 1
				if grade > score:
					score = grade
	if count >= limit:
		score = max
	return score


def match_keywords(text, keywords):
	count = 0
	text = str(text)
	for grade, tags in keywords.items():
		for tag in tags:
			if tag in text:
				print('  hit: ' + tag)
				count += 1
	if count >= 6:
		score = 10
	elif count >= 3:
		score = 8
	else:
		score = 6
	return score


def match_gpa(text, min_score, max_score):
	tags = [u'gpa', u'绩点']
	score = min_score
	text = str(text)
	for tag in tags:
		idx = [ans.start() for ans in re.finditer(tag, text.lower())]
		if len(idx) == 0:
			continue
		else:
			print('  hit: ' + tag)
			for i in range(len(idx)):
				string = text[idx[i]:idx[i] + 30]  # parse 30 characters after tag
				match = re.compile(r'\d+(?:\.\d+)?(?:\s?/\s?\d+)?', re.UNICODE)
				results = match.findall(string)
				if len(results) == 0:
					continue
				result = str(results[0])
				if result.find('/') == -1:
					continue
				[gpa, scale] = [float(num) for num in (result.split('/'))]
				if scale == 100:
					score = max(score, min(int(gpa / 5) - 13, max_score))
				elif scale == 4:
					score = max(score, min(int(gpa / 0.2) - 14, max_score))
	return score


def match_test(text, min_score, max_score):
	keywords = {
		1: [u'cet6', u'cet-6', u'六级'],
		2: [u'toefl', u'托福'],
		3: [u'ielts', u'雅思'],
	}
	score = min_score
	text = str(text)
	for test, tags in keywords.items():
		for tag in tags:
			idx = [ans.start() for ans in re.finditer(tag, text.lower())]
			if len(idx) == 0:
				continue
			else:
				print('  hit: ' + tag)
				for i in range(len(idx)):
					string = text[idx[i]:idx[i] + 30]  # parse 30 characters after tag
					match = re.compile(r'\d+(?:\.\d+)?(?:\s?/\s?\d+)?', re.UNICODE)
					results = match.findall(string)
					if len(results) == 0:
						continue
					result = str(results[0])
					if result.find('/') == -1:
						grade = float(result)
					else:
						[grade, scale] = [float(num) for num in (result.split('/'))]

					if test == 1:  # cet-6
						score = max(score, min(int(grade / 100) - 1, max_score))
					elif test == 2:  # toefl
						score = max(score, min(int(grade / 10) - 5, max_score))
					elif test == 3:  # ielts
						score = max(score, min(int(grade - 2.5), max_score))
	return score


def processResume(filename):
	print(filename + '\n**************************')
	text = convert_pdf_to_txt(filename)
	score = 0
	MAX_LIMIT = 1024
	university_score = parse_keywords(text, university_keywords, 2, 8, 20)
	print('//university_score: %d/20\n**************************' % university_score)
	job_score = parse_keywords(text, job_keywords, 3, 0, 30)
	print('//job_score: %d/30\n**************************' % job_score)
	work_score = match_keywords(text, work_keywords)
	print('//work_score: %d/10\n**************************' % work_score)
	leadership_score = parse_keywords(text, leadership_keywords, MAX_LIMIT, 6, 10)
	print('//leadership_score: %d/10\n**************************' % leadership_score)
	degree_score = parse_keywords(text, degree_keywords, MAX_LIMIT, 4, 10)
	print('//degree_score: %d/10\n**************************' % degree_score)
	study_score = max(match_gpa(text, 2, 5), parse_keywords(text, study_keywords, MAX_LIMIT, 2, 5))
	print('//study_score: %d/5\n**************************' % study_score)
	skill_score = parse_keywords(text, skill_keywords, MAX_LIMIT, 3, 5)
	print('//skill_score: %d/5\n**************************' % skill_score)
	major_score = parse_keywords(text, major_keywords, MAX_LIMIT, 3, 5)
	print('//major_score: %d/5\n**************************' % major_score)
	language_score = max(match_test(text, 3, 5), parse_keywords(text, language_keywords, MAX_LIMIT, 3, 5))
	print('//language_score: %d/5\n**************************' % language_score)
	score += university_score
	score += job_score
	score += work_score
	score += leadership_score
	score += degree_score
	score += study_score
	score += skill_score
	score += major_score
	score += language_score
	print('final score: %d/100' % score)

	return score


if len(sys.argv) == 2:
	path = sys.argv[1]

	if os.path.isfile(path) and path[-4:] == '.pdf':
		try:
			processResume(path)
		except:
			print('error')
	elif os.path.isdir(path):
		fileList = os.walk(path)
		for root, dirs, files in fileList:
			for fname in files:
				path = os.path.join(root, fname)
				if os.path.isfile(path) and path[-4:] == '.pdf':
					processResume(path)
