#!/usr/bin/env python3

import requests
from urllib import request
from lxml import etree
import sys, time

def dd(d):
	print(d)
	sys.exit()

def main():
	base_url = 'https://pic.netbian.com';
	i = 1
	while 1:
		page = '/4kmingxing/index'
		if i > 1:
			page = page + '_%s' % (i)
			
		url = base_url + '%s.html' % (page)
		print(url)
		result = requests.get(url).text
		data = etree.HTML(result)
		lis = data.xpath('//ul[@class="clearfix"]//li//a/@href')
		if not lis:
			print("扫描完成")
			break
		for l in lis:
			img_url = base_url + l
			img_res = requests.get(img_url)
			img_res.encoding = img_res.apparent_encoding
			imgs = img_res.text
			img_data = etree.HTML(imgs)
			img_info = img_data.xpath('//a[@id="img"]//img')[0]
			name = img_info.xpath('./@alt')[0]
			name_url = base_url + '%s' % (img_info.xpath('./@src')[0])
			try:
				request.urlretrieve(name_url, 'img/bizhi/' + name + '.jpg')
			except Exception as e:
				pass
			print("<%s> 下载完成" %name)
			time.sleep(1)
		i+=1
		print(i)


if __name__ == "__main__":
	main()