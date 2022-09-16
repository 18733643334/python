#!/usr/bin/env python3

import requests, json, os, sys
from urllib import request

def dd(d = ''):
	print(d)
	sys.exit()

def main(url):
	response = requests.get(url)
	res_json = response.json()
	add_path = './img/王者荣耀/'
	for i in res_json:
		c_name = i['cname']
		e_name = i['ename']
		create_dir = add_path + c_name
		if not os.path.exists(create_dir):
			os.makedirs(create_dir)
		for j in range(1, 10): 
			pic_url = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/%s/%s-bigskin-%s.jpg" % (e_name, e_name, j)
			check_status = requests.get(pic_url).status_code
			if check_status != 200 :
				continue
			img_name = c_name + '%s.jpg' % (j)
			request.urlretrieve(pic_url, create_dir + '/' + img_name)
			print(pic_url)


if __name__ == "__main__":
	
	url = "https://pvp.qq.com/web201605/js/herolist.json"
	main(url)