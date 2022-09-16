import requests
from lxml import etree
from urllib import request
import time
import sys


def main():
	url = 'http://www.huya.com/g/4079'
	
	result = requests.get(url).text
	data = etree.HTML(result)
	lists = data.xpath('//img[@class="pic"]')
	for i in lists:
		img = i.xpath('./@data-original')[0]
		name = i.xpath('./@alt')[0]
		
		img_url = img.split('?')[0]
		
		
		
		try:
			request.urlretrieve(img_url, 'img/huya/' + name + '.jpg')
		except Exception as e:
			pass
			
		print("<%s> 下载完成" %name)
		
		time.sleep(1)
		
	


if __name__ == "__main__":
	main()
	