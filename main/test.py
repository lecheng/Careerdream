import xlrd
import pickle
import simplejson

workbook = xlrd.open_workbook('shanghai.xlsx')
worksheet = workbook.sheet_by_index(0)
num_rows = worksheet.nrows - 1
curr_rows = -1
l1 = list()
while curr_rows < num_rows:
	curr_rows += 1
	row = worksheet.row(curr_rows)
	l1.append(row[0].value)
workbook = xlrd.open_workbook('beijing.xls')
worksheet = workbook.sheet_by_index(0)
num_rows = worksheet.nrows - 1
curr_rows = -1
l2 = list()
while curr_rows < num_rows:
	curr_rows += 1
	row = worksheet.row(curr_rows)
	l2.append(row[0].value)
d = {
	'beijing': l2,
	'shanghai': l1
}
with open('uber_coupons.json', 'w') as f:
 	simplejson.dump(d, f)
# with open('uber_QRcode.json', 'rb') as f:
# 	d = pickle.load(f)
# 	# unpickler = pickle.Unpickler(f)
# 	# d = unpickler.load()
# 	print(d)
# 	print(len(d['shanghai']))

with open('uber_coupons.json', 'r') as f:
	json = simplejson.load(f)
	print(len(json['beijing']))
	coupons = json['beijing'].pop()
	# simplejson.dump(json, f)
	print(len(json['beijing']))
	print(coupons)


with open('uber_coupons.json', 'w') as f:
	simplejson.dump(json, f)
