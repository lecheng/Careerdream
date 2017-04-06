import simplejson


def get_uber_coupons(city):
	with open('/opt/deploy/careerdream_v3/py/toolbox/uber_coupons.json', 'r') as f:
		json = simplejson.load(f)
		coupons = json[city].pop()
		# simplejson.dump(json, f)


	with open('/opt/deploy/careerdream_v3/py/toolbox/uber_coupons.json', 'w') as f:
		simplejson.dump(json, f)
	return coupons

if __name__ == '__main__':
	u = get_uber_coupons()
	print(u)
